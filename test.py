from team4958_customs.utilities.project_builder import Build
from team4958_customs.utils import MISSING, ROOT

import pathlib
import inspect



rootconf={
    'host': 'localhost',
    'user': 'root',
    'passwd': ''
}
dbconf={
    'host': 'localhost',
    'user': 'broadcasts_admin',
    'user2': 'broadcasts_editor',
    'passwd': r'28D%u9Xr%9ES',
    'passwd2': r'28D%u9Xr%9ES',
    'database': 'stream_notification_bot',
    'tables':[
        'Streamers (id BIGINT, link TEXT)',
        'Stream_room_data (member_id BIGINT, channel_id BIGINT, message_id BIGINT, link TEXT)'
    ]
}



# try:
#     sql.Administration(dbconf, mysql_config=rootconf).create_users()
#     print('i fckingg did it')
# except Exception as err:
#     print(err)

#Build.blank()

# def aboba():
#     name = input()
#     for sym in name:
#         if sym in _ProjectnameSymbols.allowed():
#             pass
#         else:
#             print(sym)
# aboba()

def some_recursive():
    var = input()
    if var=='stop':
        return var
    else:
        return some_recursive()

print(some_recursive())