import pandas as pd

# Read in file
df = pd.read_csv('sales_data.csv')

print(df.duplicated())

# Clean code by removing duplicate and na values
df = df.drop_duplicates()
df = df.dropna

#print(df.head().to_string()) 