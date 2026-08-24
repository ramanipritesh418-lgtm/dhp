"""

Q.1 [10 Marks]

Question:

Write a Python script to perform the following operations on Transport.

1.Create Transport(VehicleID, VehicleType, DriverName, Route, Charges).

2.Insert at least 8 records.

3.Display all vehicles operating on "Route-A".

4.Update Charges by +500 for all "Bus" VehicleType.

5.Draw a pie chart showing Charges distribution by VehicleType.

"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Database Connection
con = sqlite3.connect("Transport.db")

print("Database Connected Successfully.")

# Create Transport Table
con.execute("""
    CREATE TABLE IF NOT EXISTS Transport(
        VehicleID INTEGER,
        VehicleType TEXT,
        DriverName TEXT,
        Route TEXT,
        Charges INTEGER
    )
""")

con.commit()

print("Transport Table Created.")

# Insert 8 Records
records = [
    (1, 'Bus', 'Amit', 'Route-A', 2000),
    (2, 'Car', 'Rahul', 'Route-B', 1500),
    (3, 'Bus', 'Vijay', 'Route-A', 2500),
    (4, 'Van', 'Raj', 'Route-C', 1800),
    (5, 'Bus', 'Karan', 'Route-B', 3000),
    (6, 'Car', 'Milan', 'Route-A', 1200),
    (7, 'Van', 'Jay', 'Route-C', 2200),
    (8, 'Bus', 'Ravi', 'Route-A', 2800)
]

con.executemany(
    "INSERT INTO Transport VALUES(?,?,?,?,?)",
    records
)

con.commit()

print("8 Records Inserted.")

# Display Route-A Vehicles
df = pd.read_sql_query(
    "SELECT * FROM Transport WHERE Route='Route-A'",
    con
)

print("\nVehicles Operating on Route-A:")
print(df)

# Update Bus Charges by 500
con.execute("""
    UPDATE Transport
    SET Charges = Charges + 500
    WHERE VehicleType = 'Bus'
""")

con.commit()

print("\nBus Charges Updated by Rs.500.")

# Display Updated Records
df = pd.read_sql_query(
    "SELECT * FROM Transport",
    con
)

print("\nUpdated Transport Records:")
print(df)

# Prepare Data for Pie Chart
df = pd.read_sql_query("""
    SELECT VehicleType,
           SUM(Charges) AS TotalCharges
    FROM Transport
    GROUP BY VehicleType
""", con)

# Draw Pie Chart
plt.pie(
    df["TotalCharges"],
    labels=df["VehicleType"],
    autopct="%1.1f%%"
)

plt.title("Charges Distribution by VehicleType")
plt.show()

print("\nPie Chart Displayed Successfully.")


"""
====== Output Q.1 ======

Database Connected Successfully.
Transport Table Created.
8 Records Inserted.

Vehicles Operating on Route-A:

   VehicleID VehicleType DriverName    Route  Charges
0          1         Bus       Amit  Route-A     2000
1          3         Bus      Vijay  Route-A     2500
2          6         Car      Milan  Route-A     1200
3          8         Bus       Ravi  Route-A     2800

Bus Charges Updated by Rs.500.

Updated Transport Records:

   VehicleID VehicleType DriverName    Route  Charges
0          1         Bus       Amit  Route-A     2500
1          2         Car      Rahul  Route-B     1500
2          3         Bus      Vijay  Route-A     3000
3          4         Van        Raj  Route-C     1800
4          5         Bus      Karan  Route-B     3500
5          6         Car      Milan  Route-A     1200
6          7         Van        Jay  Route-C     2200
7          8         Bus       Ravi  Route-A     3300

Pie Chart Displayed Successfully.

"""


"""

Q.2 [10 Marks]

Question:

Create table Restaurant(OrderID, Customer, Dish, Quantity, BillAmount) and add at least 6 records.

Write a Python code to do the following:

1.Export the table into a CSV file restaurant.xlsx.

2.Retrieve all orders where Quantity > 3.

3.Drop the table Restaurant.

4.Import the CSV data back into a new table Restaurant_New.

"""

import sqlite3
import pandas as pd

# Database Connection
con = sqlite3.connect("Restaurant.db")

print("Database Connected Successfully.")

# Create Restaurant Table
con.execute("""
    CREATE TABLE IF NOT EXISTS Restaurant(
        OrderID INTEGER,
        Customer TEXT,
        Dish TEXT,
        Quantity INTEGER,
        BillAmount INTEGER
    )
""")

con.commit()

print("Restaurant Table Created.")

# Insert 6 Records
records = [
    (1, 'Amit', 'Pizza', 2, 400),
    (2, 'Rahul', 'Burger', 5, 500),
    (3, 'Vijay', 'Dosa', 4, 320),
    (4, 'Neha', 'Sandwich', 2, 200),
    (5, 'Karan', 'Biryani', 6, 900),
    (6, 'Riya', 'Pasta', 3, 450)
]

con.executemany(
    "INSERT INTO Restaurant VALUES(?,?,?,?,?)",
    records
)

con.commit()

print("6 Records Inserted.")

# Retrieve Orders where Quantity > 3
df = pd.read_sql_query(
    "SELECT * FROM Restaurant WHERE Quantity > 3",
    con
)

print("\nOrders where Quantity is greater than 3:")
print(df)

# Export Restaurant Table to CSV
df = pd.read_sql_query(
    "SELECT * FROM Restaurant",
    con
)

df.to_csv("restaurant.csv", index=False)

print("\nData Exported to CSV.")

# Drop Restaurant Table
con.execute("DROP TABLE Restaurant")

con.commit()

print("Restaurant Table Dropped.")

# Import CSV Data into Restaurant_New
df = pd.read_csv("restaurant.csv")

df.to_sql(
    "Restaurant_New",
    con,
    if_exists="replace",
    index=False
)

print("CSV Data Imported into Restaurant_New.")

# Display Restaurant_New Table
df = pd.read_sql_query(
    "SELECT * FROM Restaurant_New",
    con
)

print("\nRestaurant_New Records:")
print(df)


"""
====== Output Q.2 ======

Database Connected Successfully.
Restaurant Table Created.
6 Records Inserted.

Orders where Quantity is greater than 3:

   OrderID Customer     Dish  Quantity  BillAmount
0        2    Rahul   Burger         5         500
1        3    Vijay     Dosa         4         320
2        5    Karan  Biryani         6         900

Data Exported to CSV.
Restaurant Table Dropped.
CSV Data Imported into Restaurant_New.

Restaurant_New Records:

   OrderID Customer      Dish  Quantity  BillAmount
0        1     Amit     Pizza         2         400
1        2    Rahul    Burger         5         500
2        3    Vijay      Dosa         4         320
3        4     Neha  Sandwich         2         200
4        5    Karan   Biryani         6         900
5        6     Riya     Pasta         3         450

"""