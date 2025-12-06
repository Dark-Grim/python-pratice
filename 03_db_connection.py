from sqlalchemy import create_engine, inspect

# Creating Engine
engine = create_engine("sqlite:///Database/Chinook.sqlite")

# Get Table Names
insp = inspect(engine)
tables = insp.get_table_names()
print(tables)
