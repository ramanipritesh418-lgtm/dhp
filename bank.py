# ==========================================================
# Q.1 Write a python script to create database "Bank.db"
# and perform following task.
#
# A. Create table Customer(c_id, name, act_type, balance).
# B. Insert 10 records.
# C. Read data into Data Frame.
# D. Display customer id and balance whose name starts with 'A'.
# E. Display last 3 records.
# ==========================================================


import sqlite3
import pandas as pd


# Create Database
con = sqlite3.connect("Bank.db")

print("Database Created Successfully.")


# A. Create Customer Table
con.execute("CREATE TABLE IF NOT EXISTS Customer(c_id, name, act_type, balance)")


# ==========================================================
# B. Insert 10 Records
#
# METHOD 1: Simple Method
# ==========================================================

# con.execute("INSERT INTO Customer VALUES(1, 'Amit', 'Saving', 5000)")
# con.execute("INSERT INTO Customer VALUES(2, 'Rahul', 'Current', 8000)")
# con.execute("INSERT INTO Customer VALUES(3, 'Ankit', 'Saving', 6500)")
# con.execute("INSERT INTO Customer VALUES(4, 'Bhavik', 'Saving', 4500)")
# con.execute("INSERT INTO Customer VALUES(5, 'Chetan', 'Current', 9000)")
# con.execute("INSERT INTO Customer VALUES(6, 'Dhruv', 'Saving', 7200)")
# con.execute("INSERT INTO Customer VALUES(7, 'Ajay', 'Current', 5500)")
# con.execute("INSERT INTO Customer VALUES(8, 'Kiran', 'Saving', 3000)")
# con.execute("INSERT INTO Customer VALUES(9, 'Mehul', 'Current', 8500)")
# con.execute("INSERT INTO Customer VALUES(10, 'Ravi', 'Saving', 6000)")


# ==========================================================
# METHOD 2: Shortcut Method
# ==========================================================

data = [
    (1, 'Amit', 'Saving', 5000),
    (2, 'Rahul', 'Current', 8000),
    (3, 'Ankit', 'Saving', 6500),
    (4, 'Bhavik', 'Saving', 4500),
    (5, 'Chetan', 'Current', 9000),
    (6, 'Dhruv', 'Saving', 7200),
    (7, 'Ajay', 'Current', 5500),
    (8, 'Kiran', 'Saving', 3000),
    (9, 'Mehul', 'Current', 8500),
    (10, 'Ravi', 'Saving', 6000)
]

con.executemany("INSERT INTO Customer VALUES (?, ?, ?, ?)", data)


# Save Changes
con.commit()


# ==========================================================
# C. Read data into DataFrame
# ==========================================================

df = pd.read_sql_query("SELECT * FROM Customer", con)
print(df)


# ==========================================================
# D. Display customer id and balance whose name starts with 'A'
# ==========================================================

df = pd.read_sql_query(
    "SELECT c_id, balance FROM Customer WHERE name LIKE 'A%'",
    con
)
print(df)


# ==========================================================
# E. Display last 3 records
# ==========================================================

df = pd.read_sql_query(
    "SELECT * FROM Customer ORDER BY c_id DESC LIMIT 3",
    con
)
print(df)
