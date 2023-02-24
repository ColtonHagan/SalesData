import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Header function for organising data
def header(str):
    out = ""
    size = 30
    filler = size - len(str)
    for i in range(filler):
        if(len(str) != 0 and i == round(filler/2)):
            out += str
        else:
            if(i % 2 == 0):
                out += "+"
            else:
                out += "="
    return out

# Read in file
df = pd.read_csv("sales_data.csv")

# Clean code by removing duplicate, na values, and combining sales when multiple for same day listed
df = df.drop_duplicates()
df = df.dropna()
df = df.groupby(['date', 'product', 'store'])['sales'].sum().reset_index()

# Also changes date format since I like this better
df["date"] = pd.to_datetime(df['date']).dt.strftime('%m/%d/%y')

# Print basic data for everything
print(header("Misc info"))
max = df.max()
print("Highest sales day: {} with {} sales".format(max["date"], max["sales"]))
sum = df["sales"].sum()
print("Total sales: " + str(sum))

# Print about Amazon sales
print(header("Amazon sales"))
amazon_df = df[df["store"] == "Amazon"]
amazon_df = amazon_df.groupby("product").mean().round(2)
print(amazon_df.to_string())

# Print graph
print(header("Product graph"))

# Group the data by product
groups = df.groupby("product")
fig, ax = plt.subplots()
for name, group in groups:
    group.plot(x="date", y="sales", ax=ax, label=name)
plt.xlabel("Date", size=15)
plt.xticks(fontsize=8, rotation=90)
plt.yticks(fontsize=8)
plt.ylabel("Sales", size=15)
plt.title("Sales per day", size=20)

# Show the legend
plt.legend(loc="best")

# Display the plot
plt.show()

# I could add some summery data here, but i know how and don't want to
 
df.to_csv('clean_sales_data.csv', index=False)

print(header(""))