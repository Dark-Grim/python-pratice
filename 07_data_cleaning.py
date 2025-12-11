import pandas as pd
import datetime as dt

# Reading messy_data csv
df = pd.read_csv("./Data/messy_data.csv")

# Check info
# print(df.info())

# Covert purchase_amount datatype to int after cleaning
df["purchase_amount"] = (
    df["purchase_amount"]
    .str.replace(r"INR", "", regex=True)
    .str.replace(r"[₹,]", "", regex=True)
    .str.strip()
)

# Replaced NaN with 0 and converted type to int
df["purchase_amount"] = df["purchase_amount"].fillna(0).astype("int")

# Assertion check
assert df["purchase_amount"].dtype == "int"

# Check total purchase amount if assertion is True
print(df["purchase_amount"].sum())
