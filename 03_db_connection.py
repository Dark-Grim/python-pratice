from sqlalchemy import create_engine, inspect, text
import pandas as pd


# Creating Engine
engine = create_engine("sqlite:///Database/Chinook.sqlite")


# Get Table Names
insp = inspect(engine)
tables = insp.get_table_names()
print("Table Names:", tables)


# Querying Database
with engine.connect() as con:
    rs = con.execute(text("SELECT * FROM Customer"))
    df = pd.DataFrame(rs.fetchall())
    print(df.head())


# TODO

# Execute the query that selects all records from the Employee table where 'EmployeeId' is greater than or equal to 6.
# Use the >= operator and assign the results to rs.
# Apply the method fetchall() to rs in order to fetch all records in rs. Store them in the DataFrame df.
# Using the rs object, set the DataFrame's column names to the corresponding names of the table columns.

with engine.connect() as con:
    rs = con.execute(text("SELECT * FROM Employee WHERE EmployeeId >= 6"))
    df = pd.DataFrame(rs.fetchall())
    print(df.head())


# We can achieve the Above result by only using Pandas
df1 = pd.read_sql_query("SELECT * FROM Employee WHERE EmployeeId >= 6", engine)

# Check it df and df1 are same
print("Check for comparison between DataFrame Results:", df1.equals(df))


# Joining Tables
# TODO

# select the Title of the record and Name of the artist of each record from the Album table and the Artist table, respectively.
# To do so, INNER JOIN these two tables on the ArtistID column of both.

df = pd.read_sql_query(
    "SELECT Album.Title, Artist.Name FROM Album INNER JOIN Artist ON Album.ArtistId = Artist.ArtistId",
    engine,
)
print(df.head())
