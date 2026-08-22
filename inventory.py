# ============================================================
# Q.1 Create "Inventory" table in SQLite3 with appropriate
# constraints.
#
# Inventory (item_id, item_name, category, qty, unit_price)
#
# A. Insert 10 records with appropriate category.
# B. Export table data to csv file & Load CSV file In python.
# C. Find Total Inventory Value.
# ============================================================


import sqlite3
import pandas as pd


# -------------------- CREATE DATABASE --------------------

con = sqlite3.connect("Inventory.db")

print("Database Created Successfully.")


# -------------------- CREATE TABLE --------------------

con.execute("""
CREATE TABLE IF NOT EXISTS Inventory(
    item_id INTEGER PRIMARY KEY,
    item_name TEXT NOT NULL,
    category TEXT NOT NULL,
    qty INTEGER NOT NULL,
    unit_price REAL NOT NULL
)
""")


# -------------------- INSERT 10 RECORDS --------------------
# Shortcut Method

data = [
    (1, 'Laptop', 'Electronics', 5, 50000),
    (2, 'Mouse', 'Electronics', 20, 500),
    (3, 'Keyboard', 'Electronics', 15, 1200),
    (4, 'Chair', 'Furniture', 10, 3500),
    (5, 'Table', 'Furniture', 6, 7000),
    (6, 'Notebook', 'Stationery', 50, 80),
    (7, 'Pen', 'Stationery', 100, 20),
    (8, 'Printer', 'Electronics', 3, 15000),
    (9, 'Bag', 'Accessories', 12, 1200),
    (10, 'Bottle', 'Accessories', 25, 400)
]

con.executemany(
    "INSERT INTO Inventory VALUES (?, ?, ?, ?, ?)",
    data
)

con.commit()


# -------------------- SIMPLE METHOD --------------------
# Reference Only - Do NOT run with the above method

# con.execute("INSERT INTO Inventory VALUES(1,'Laptop','Electronics',5,50000)")
# con.execute("INSERT INTO Inventory VALUES(2,'Mouse','Electronics',20,500)")
# con.execute("INSERT INTO Inventory VALUES(3,'Keyboard','Electronics',15,1200)")
# con.execute("INSERT INTO Inventory VALUES(4,'Chair','Furniture',10,3500)")
# con.execute("INSERT INTO Inventory VALUES(5,'Table','Furniture',6,7000)")
# con.execute("INSERT INTO Inventory VALUES(6,'Notebook','Stationery',50,80)")
# con.execute("INSERT INTO Inventory VALUES(7,'Pen','Stationery',100,20)")
# con.execute("INSERT INTO Inventory VALUES(8,'Printer','Electronics',3,15000)")
# con.execute("INSERT INTO Inventory VALUES(9,'Bag','Accessories',12,1200)")
# con.execute("INSERT INTO Inventory VALUES(10,'Bottle','Accessories',25,400)")


# -------------------- EXPORT TO CSV --------------------

df = pd.read_sql_query("SELECT * FROM Inventory", con)

df.to_csv("Inventory.csv", index=False)

print("\nInventory data exported to CSV successfully.")


# -------------------- LOAD CSV IN PYTHON --------------------

df = pd.read_csv("Inventory.csv")

print("\nData Loaded From CSV:")
print(df)


# -------------------- TOTAL INVENTORY VALUE --------------------

df["total"] = df["qty"] * df["unit_price"]

total_value = df["total"].sum()

print("\nTotal Inventory Value =", total_value)


# ============================================================
# OUTPUT
# ============================================================

# Database Created Successfully.
#
# Inventory data exported to CSV successfully.
#
# Data Loaded From CSV:
#
#    item_id item_name      category  qty  unit_price
# 0        1    Laptop   Electronics    5     50000.0
# 1        2     Mouse   Electronics   20       500.0
# 2        3  Keyboard   Electronics   15      1200.0
# 3        4     Chair     Furniture   10      3500.0
# 4        5     Table     Furniture    6      7000.0
# 5        6  Notebook    Stationery   50        80.0
# 6        7       Pen    Stationery  100        20.0
# 7        8   Printer   Electronics    3     15000.0
# 8        9       Bag   Accessories   12      1200.0
# 9       10    Bottle   Accessories   25       400.0
#
# Total Inventory Value = 430400.0
# ============================================================
