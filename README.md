# team4958_customs

A small collection of reusable Python helpers I originally built to reduce repetitive code in my early projects.

> **Historical project (2023).** This package was written independently during my early Python learning period, before I adopted AI-assisted coding workflows. The implementation is intentionally preserved largely as it was written at the time instead of being rewritten to modern standards.

## Why this project exists

While building bots and small utilities, I repeatedly found myself copying the same setup, database and project-scaffolding code between projects. `team4958_customs` grew from an attempt to extract those repeated patterns into reusable helpers that could be installed as a Python package.

The project reached version `0.2.5` and was packaged with Poetry for installation through `pip`.

## What is inside

### Async and threading helpers

`team4958_customs.tools.asyncs`

Early wrappers around `asyncio` and `threading` intended to shorten common calls and reduce repeated exception-handling code.

### MySQL helpers

`team4958_customs.tools.sql`

Helpers around `mysql-connector-python` for common query flows such as connect → execute → fetch/commit → disconnect, plus early database-administration utilities.

### Project scaffolding

`team4958_customs.utilities.project_builder`

Utilities for generating project structures from dictionaries or built-in presets. One of the presets scaffolds a Disnake bot project with a basic extension layout, logging setup and configuration files.

### Small utilities

`team4958_customs.utils` and `team4958_customs.utilities.common`

Miscellaneous helpers and sentinels used across the package.

## Installation

```bash
python -m pip install team4958-customs
```

Or install the repository locally:

```bash
python -m pip install .
```

## Example: MySQL helper

```python
from team4958_customs.tools.sql import MySQLqueries

config = {
    "host": "localhost",
    "user": "app_user",
    "passwd": "example-password",
    "database": "example_db",
}

sql = MySQLqueries(config)
rows = sql.fetch_all("SELECT * FROM example_table")
```

The SQL helper accepts raw SQL strings. As with any raw-query API, parameterization and input validation remain the caller's responsibility.

## Example: project builder

```python
from team4958_customs.utilities.project_builder import Build

Build.blank(name="my_project")
```

The builder can also create a directory structure from a nested dictionary or use one of the bundled presets.

## Project status

**Historical / learning project. Not recommended for new production use.**

This repository is useful primarily as a record of my earlier hands-on Python work and the progression from small repeated snippets toward reusable abstractions and installable packages.

The code intentionally retains early design decisions and limitations. I would approach several areas differently today, including event-loop lifecycle management, thread APIs, SQL parameterization, dependency isolation and automated testing.

## Development history

This project predates my current AI-assisted development workflow and was written independently. Documentation and repository presentation were cleaned up later for portfolio use, while the implementation itself remains substantially historical.

## License

MIT License.
