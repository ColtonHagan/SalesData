#Creates csv file for project

import pandas as pd
import numpy as np

# Set error values percentage
err_pct = 5

# Generate random date range
start_date = pd.Timestamp('2022-01-01').normalize()
end_date = pd.Timestamp('2022-12-31').normalize()
num_days = np.random.randint(30, 90)
dates = pd.date_range(start_date, end_date, periods=num_days)

# Generate random sales data for the date range
products = ['iPhone', 'Samsung Galaxy', 'Google Pixel', 'LG', 'Motorola']
stores = ['Best Buy', 'Walmart', 'Target', 'Amazon', 'Apple Store']

# Create dictionary to hold data
data_dict = {
    'date': [],
    'product': [],
    'store': [],
    'sales': []
}

# Create columns and generate missing values in random locations
for i in range(num_days):
    for j in range(np.random.randint(1, 4)):
        data_dict['date'].append(dates[i].date())
        data_dict['product'].append(np.random.choice(products))
        data_dict['store'].append(np.random.choice(stores))
        # Random null values
        if np.random.random() < (err_pct / 100):
            data_dict['sales'].append(np.nan)
        else:
            data_dict['sales'].append(np.random.randint(100, 1000))
        # Duplicate the row with the same data
        if np.random.random() < (err_pct / 100):
            data_dict['date'].append(dates[i].date())
            data_dict['product'].append(data_dict['product'][-1])
            data_dict['store'].append(data_dict['store'][-1])
            data_dict['sales'].append(data_dict['sales'][-1])

# Create dataframe from dictionary
sales_data = pd.DataFrame(data_dict)

# Save the data to a CSV file
sales_data.to_csv('sales_data.csv', index=False)

print("sales_data.csv created.")
