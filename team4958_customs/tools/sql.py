"""
MySQL work simplification
---------
"""



import mysql.connector
from mysql.connector import Error as sqlErr

from team4958_customs.utils import *

import logging, traceback



__all__ = [
    'MySQLqueries',
    'Administration'
]
log = logging.getLogger(__name__)



class MySQLqueries():
    """
    basic one-srting MySQL queries
    -------
    \n
    works as `connect->execute query->commit if necessary->disconnect`\n
    helps to avoid freaking bunches of unused connections\n
    --------------------------\n
    dbconfig: your database config as `dict`{\n
        `'host'`: host address as str,\n
        `'user'`: db primary user username,\n
        `'passwd'`: db primary user password,\n
        `'user2'`: db secondary user username,\n
        `'passwd2'`: db secondary user password,\n
        `'database'`: your database name,\n
        `'tables'`: db tables structure presented as ['table (column TYPE, column TYPE, etc.)', etc.]\n
        }\n
    alt_user: specify if you need to set this parameter to whole class instance
    """

    def __init__(self, dbconfig:dict, alt_user=False):
        self.dbconfig = dbconfig
        self.alt_user=alt_user
    
    def commitable(self, sql_query:str, alt_user: bool=MISSING):
        """
        commit-requiring query\n
        has no output\n
        -----\n
        sql_query: MySQL query to execute\n
        alt_user: specify if you need to set for this call only
        """
        if alt_user is MISSING:
            alt_user=self.alt_user
        conn = BasicAction().connect(self.dbconfig, secondary=alt_user)
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute(sql_query)
                conn.commit()
            except sqlErr as err:
                log.error(f"failed commitable query: {sql_query}\n{err}", exc_info=True)
                print(f"failed commitable query: {sql_query}")
                traceback.print_exc()
            finally:
                cursor.close()
                conn.close()
    
    def fetch_one(self, sql_query:str, alt_user: bool=MISSING):
        """
        not commit-requiring query\n
        fetchone as output (returns tuple)\n
        -----\n
        alt_user: specify if you need to set for this call only
        """
        if alt_user is MISSING:
            alt_user=self.alt_user
        conn = BasicAction().connect(self.dbconfig, secondary=alt_user)
        if conn:
            cursor = conn.cursor()
            res = MISSING
            try:
                cursor.execute(sql_query)
                res = cursor.fetchone()
            except sqlErr as err:
                log.error(f"failed fetchable query: {sql_query}\n{err}", exc_info=True)
                print(f"failed fetchable query: {sql_query}")
                traceback.print_exc()
            finally:
                cursor.close()
                conn.close()
            return res
        else:
            return

    def fetch_all(self, sql_query:str, alt_user: bool=MISSING):
        """
        not commit-requiring query\n
        fetchall as output (returns list of tuples)\n
        -----\n
        alt_user: specify if you need to set for this call only
        """
        if alt_user is MISSING:
            alt_user=self.alt_user
        conn = BasicAction().connect(self.dbconfig, secondary=alt_user)
        if conn:
            cursor = conn.cursor()
            res = MISSING
            try:
                cursor.execute(sql_query)
                res = cursor.fetchall()
            except sqlErr as err:
                log.error(f"failed fetchable query: {sql_query}\n{err}", exc_info=True)
                print(f"failed fetchable query: {sql_query}")
                traceback.print_exc()
            finally:
                cursor.close()
                conn.close()
            return res
        else:
            return
    
    def fetch_many(self, sql_query:str, size:int, alt_user: bool=MISSING):
        """
        not commit-requiring query\n
        fetchmany as output (returns list of tuples)\n
        -----\n
        size: amount of elements to fetch from database\n
        alt_user: specify if you need to set for this call only
        """
        if alt_user is MISSING:
            alt_user=self.alt_user
        conn = BasicAction().connect(self.dbconfig, secondary=alt_user)
        if conn:
            cursor = conn.cursor()
            res = MISSING
            try:
                cursor.execute(sql_query)
                res = cursor.fetchmany(size=size)
            except sqlErr as err:
                log.error(f"failed fetchable query: {sql_query}\n{err}", exc_info=True)
                print(f"failed fetchable query: {sql_query}")
                traceback.print_exc()
            finally:
                # cursor.close()
                conn.close()
            return res
        else:
            return



class Administration():
    """
    MySQL administration simplification
    -------
    \n
    works as `connect->execute preset queries->commit if necessary->disconnect`\n
    automates some boring processes like database or user creation for example\n
    --------------------------\n
    dbconfig: your database config as `dict`{\n
        `'host'`: host address as str (must be same as in mysql_config),\n
        `'user'`: db primary user username,\n
        `'passwd'`: db primary user password,\n
        `'user2'`: db secondary user username,\n
        `'passwd2'`: db secondary user password,\n
        `'database'`: your database name,\n
        `'tables'`: db tables structure presented as ['table (column TYPE, column TYPE, etc.)', etc.]\n
        }\n
    --------------------------\n
    mysql_config: your deafult mysql config as `dict`{\n
        `'host'`: host address as str,\n
        `'user'`: db root or admin user username,\n
        `'passwd'`: db root or admin user password,\n
        }\n
    this arg is required only when you set 'root' as True\n
    --------------------------\n
    alt_user: specify if you need to set this parameter to whole class instance
    """
    
    def __init__(self, dbconfig: dict, mysql_config: dict=MISSING, alt_user=False):
        self.dbconfig=dbconfig
        self.mysql_config=mysql_config
        self.alt_user=alt_user
    
    def create_db(self, add_users=False, add_tables=True):
        """
        creates a new database\n
        `your MySQL user must have required privileges and grant option to use this one!`\n
        ----------\n
        add_users: if you need to create new users for using this db (deafult is False)\n
        this will create 2 users, `their usernames and passwords must be specified in 'dbconfig' dict which is being given as a class arg`\n
        ------------\n
        add_tables: if you need to create some tables in this db (you probably do, right?..)\n
        tables and their structures `must be specified must be specified in 'dbconfig' dict which is being given as a class arg`
        """
        if add_users:
            conn = BasicAction().connect(self.dbconfig, root=True, rootconfig=self.mysql_config)
        else:
            conn = BasicAction().connect(self.dbconfig)
            if not conn:
                conn = BasicAction().connect(self.dbconfig, root=True, rootconfig=self.mysql_config)
        if conn:
            cursor=conn.cursor()
            try:
                cursor.execute(f"CREATE DATABASE {self.dbconfig['database']}")
                conn.commit()
            except sqlErr as err:
                log.error(f"failed creating database: {self.dbconfig['database']}\n{err}", exc_info=True)
                print(f"failed creating database: {self.dbconfig['database']}")
                traceback.print_exc()
            except Exception as err:
                log.error(f"unexpected error while creating database\n{err}", exc_info=True)
                print(f"unexpected error while creating database")
                traceback.print_exc()
            cursor.execute(f"USE {self.dbconfig['database']}")
            conn.commit()
            if add_tables:
                try:
                    self.create_tables(connection=conn)
                except:
                    pass
            if add_users:
                try:
                    self.create_users(connection=conn)
                except:
                    pass
    
    def create_users(self, connection=MISSING):
        """
        creates 2 new MySQL users which parameters (usernames and passwords) must be specified in 'dbconfig' dict which is being given as a class arg\n
        -----------\n
        connection: MySQL connection instance if you already have one (optional)\n
        `creates its own one as yor deafult MySQL user if not presented `
        """
        if connection is MISSING:
            conn = BasicAction().connect(self.dbconfig, root=True, rootconfig=self.mysql_config)
        else:
            conn = connection
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute(f"CREATE USER '{self.dbconfig['user']}'@'{self.dbconfig['host']}' IDENTIFIED BY '{self.dbconfig['passwd']}'")
                conn.commit()
                cursor.execute(f"GRANT ALL ON *.* TO '{self.dbconfig['user']}'@'{self.dbconfig['host']}' WITH GRANT OPTION")
                conn.commit()
                cursor.execute(f"FLUSH PRIVILEGES")
                conn.commit()
            except sqlErr as err:
                log.error(f"failed creating user: {self.dbconfig['user']}\n{err}", exc_info=True)
                print(f"failed creating user: {self.dbconfig['user']}")
                traceback.print_exc()
            except Exception as err:
                log.error(f"unexpected error while creating user\n{err}", exc_info=True)
                print(f"unexpected error while creating user")
                traceback.print_exc()
            try:
                cursor.execute(f"CREATE USER '{self.dbconfig['user2']}'@'{self.dbconfig['host']}' IDENTIFIED BY '{self.dbconfig['passwd2']}'")
                conn.commit()
                cursor.execute(f"GRANT ALL ON *.* TO '{self.dbconfig['user2']}'@'{self.dbconfig['host']}' WITH GRANT OPTION")
                conn.commit()
                cursor.execute(f"FLUSH PRIVILEGES")
                conn.commit()
            except sqlErr as err:
                log.error(f"failed creating user: {self.dbconfig['user2']}\n{err}", exc_info=True)
                print(f"failed creating user: {self.dbconfig['user2']}")
                traceback.print_exc()
            except Exception as err:
                log.error(f"unexpected error while creating user\n{err}", exc_info=True)
                print(f"unexpected error while creating user")
                traceback.print_exc()
            cursor.close()
            if connection is MISSING:
                conn.close()
    
    def create_tables(self, connection=MISSING, database: str=MISSING, table_listing: list=MISSING):
        """
        creates tables in your database\n
        -----------\n
        connection: MySQL connection instance if you already have one (optional)\n
        ---------------\n
        database: database to create tables in it (optional)\n
        `inherited from a class instance if not presented`\n
        --------------\n
        table_listing: db tables structure presented as ['table (column TYPE, column TYPE, etc.)', etc.] (optional)\n
        `inherited from a class instance if not presented`
        """
        if connection is MISSING:
            conn = BasicAction().connect(self.dbconfig, root=True, rootconfig=self.mysql_config)
        else:
            conn = connection
        if conn:
            cursor = conn.cursor()
            if database is MISSING:
                database = self.dbconfig['database']
            if table_listing is MISSING:
                table_listing = self.dbconfig['tables']
            if connection is MISSING:
                cursor.execute(f"USE {database}")
                conn.commit()
            else:
                db_old = conn._database
                cursor.execute(f"USE {database}")
                conn.commit()
            for table in table_listing:
                try:
                    cursor.execute(f"CREATE TABLE {table}")
                    conn.commit()
                except sqlErr as err:
                    log.error(f"{database} - failed creating table: {table}\n{err}", exc_info=True)
                    print(f"{database} - failed creating table: {table}")
                    traceback.print_exc()
                except Exception as err:
                    log.error(f"unexpected error while creating database\n{err}", exc_info=True)
                    print(f"unexpected error while creating database")
                    traceback.print_exc()
            if connection is MISSING:
                cursor.close()
                conn.close()
            else:
                cursor.execute(f"USE {db_old}")
                conn.commit()
                cursor.close()



class BasicAction():
    """
    necessary backend actions which you shouldn't call without extreme need
    -----------\n
    it may cause some global problems with your MySQL server or client
    """

    def __init__(self, alt_user=False):
        self.alt_user=alt_user

    def connect(self, dbconfig:dict, root=False, rootconfig: dict=MISSING, secondary: bool=MISSING):
        """
        `NEVER FUCKING CALL THIS INSIDE YOUR CODE`
        ------------
        \n
        otherwise you may cause MySQL connections excess!\n
        ---------\n
        connects you to database\n
        ---------\n
        root: set True if you need to use root user (no database by deafult)\n
        rootconfig: your deafult mysql config as `dict`{\n
        `'host'`: host address as str,\n
        `'user'`: db root or admin user username,\n
        `'passwd'`: db root or admin user password,\n
        }\n
        this arg is required only when you set 'root' as True\n
        --------------------------\n
        secondary: specify if you need to use a secondary user for this call only
        """
        if not root:
            if secondary is MISSING:
                secondary=self.alt_user
            try:
                connection_db = mysql.connector.connect(
                    host = dbconfig['host'],
                    user = dbconfig['user'] if not secondary else dbconfig['user2'],
                    passwd = dbconfig['passwd'] if not secondary else dbconfig['passwd2'],
                    database = dbconfig['database']
                )
                connection_db.commit()
                return connection_db
            except sqlErr as db_connection_error:
                log.error(db_connection_error, exc_info=True)
                #print("Возникла ошибка MySQL: ", db_connection_error)
                return
            except Exception as err:
                log.error(f"passing an unhandled exception:\n{err}", exc_info=True)
                print("passing an unhandled exception:")
                traceback.print_exc()
                return
        else:
            if rootconfig is MISSING:
                raise ValueError("You need to specify a 'rootconfig' arg while calling a root connection!")
            else:
                try:
                    connection_db = mysql.connector.connect(
                        host = rootconfig['host'],
                        user = rootconfig['user'],
                        passwd = rootconfig['passwd']
                    )
                    connection_db.commit()
                    return connection_db
                except sqlErr as db_connection_error:
                    log.error(db_connection_error, exc_info=True)
                    #print("Возникла ошибка MySQL: ", db_connection_error)
                    return
                except Exception as err:
                    log.error(f"passing an unhandled exception:\n{err}", exc_info=True)
                    print("passing an unhandled exception:")
                    traceback.print_exc()
                    return



class _Clear:
    """MySQL response clearer"""

    def string(obj):
        """clears response from `fetchone`"""
        chars_to_remove = ["(", ")", ",", "'"]
        element = str()
        try:
            for element in obj:
                for char in chars_to_remove:
                    element = str(element)
                    element = element.replace(char, "")
        except:
            pass
        return element
    
    def listing(obj):
        """clears response from `fetchall`"""
        chars_to_remove = ["(", ")", ",", "'"]
        clear_list = []
        try:
            for element in obj:
                for char in chars_to_remove:
                    element = str(element)
                    element = element.replace(char, "")
                clear_list.append(element)
        except:
            pass
        return clear_list