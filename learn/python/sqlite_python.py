# how to connect to sqlite3 database for practice

import sqlite3
from pathlib import Path

cwd = Path.cwd() / "learn/python"

ctx = sqlite3.connect(cwd / "test.db")  # test.db will be created or opened

cu = ctx.cursor()

# create a table
if ctx is None:
    cu.execute("create table lang(name, first_appeared)")
else:
    print("Failed to create database table")

# insert values into a table
cu.execute("insert into lang values (?, ?)", ("C", 1972))
cu.execute("insert into lang values (?, ?)", ("python", 1932))
cu.execute("insert into lang values (?, ?)", ("Erlang", 1922))
cu.execute("insert into lang values (?, ?)", ("c++", 1942))

# execute a query and iterate over the result
with open(cwd / "select_all.sql") as f:
    for row in cu.execute(f.read()):
        print(row)

# insert into a database with an insert query with placeholders
payload = {"lang_name": "Rust", "created": 1990}

with open(cwd / "insert_with_placeholders.sql") as d:
    cu.execute(d.read(), payload)

ctx.close()
