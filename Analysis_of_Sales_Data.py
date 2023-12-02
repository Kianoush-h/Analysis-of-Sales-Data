
"""
@author: Kianoush 

GitHUb: https://github.com/Kianoush-h
YouTube: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA
LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/

Email: haratiank2@gmail.com

"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns


# Load all CSV files into a list of DataFrames
file_path = 'data/sales_data_sample.csv'

# encoding = "utf-8"
encoding = "ISO-8859-1"

raw_data = pd.read_csv(file_path, encoding = encoding)

print(raw_data.shape)

# Display the first few rows
head = raw_data.head(5)

# Display the last few rows
raw_data.tail(5)

# Basic statistics of numerical columns
temp = raw_data.describe()

categorical_stats = raw_data.describe(include=['object'])


raw_data.info()

# raw_data.dropna(inplace=True)

raw_data['ORDERDATE'] = pd.to_datetime(raw_data['ORDERDATE'], infer_datetime_format=True)



# raw_data['year'] = raw_data['date_of_infraction'].dt.year
# raw_data['month'] = raw_data['date_of_infraction'].dt.month
raw_data['day_of_week'] = raw_data['ORDERDATE'].dt.dayofweek

# =============================================================================
# Data Visualization
# =============================================================================

# =============================================================================
# PART 1 
# =============================================================================


# Graph 1
month_name_mapping = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
raw_data['month_name'] = raw_data['MONTH_ID'].map(month_name_mapping)
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
raw_data['month_name'] = pd.Categorical(raw_data['month_name'], categories=months_order, ordered=True)

# Use a color palette from seaborn
sns.set_palette("viridis")

# Create the first subplot (top)
plt.figure(figsize=(12, 12))
plt.subplot(2, 1, 1)

# Line plot for Temporal Trends by Months with sorted month names
sns.lineplot(data=raw_data.groupby('month_name')['SALES'].sum().sort_index(), marker='o', linestyle='-')

# Labels and titles for the first subplot
plt.title('SALES Over the Months', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('SALES', fontsize=14)
plt.grid(True)

# Data labels for the first subplot
for index, value in enumerate(raw_data.groupby('month_name')['SALES'].sum().sort_index()):
    plt.text(index, value + 1, str(value), ha='center', va='bottom')


# Graph 2
# Use a color palette from seaborn
sns.set_palette("viridis")

# Create the second subplot (bottom)
plt.subplot(2, 1, 2)

# Line plot for Temporal Trends by Months with sorted month names
sns.lineplot(data=raw_data.groupby('month_name')['QUANTITYORDERED'].sum().sort_index(), marker='o', linestyle='-')

# Labels and titles for the second subplot
plt.title('QUANTITY ORDERED Over the Months', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('QUANTITY ORDERED', fontsize=14)
plt.grid(True)

# Data labels for the second subplot
for index, value in enumerate(raw_data.groupby('month_name')['QUANTITYORDERED'].sum().sort_index()):
    plt.text(index, value + 1, str(value), ha='center', va='bottom')

# Adjust layout to prevent clipping of titles and labels
plt.tight_layout()

# Show the plot
plt.show()



# =============================================================================
# PART 2 
# =============================================================================


# Map day_of_week numerical values to day names and sort them
day_name_mapping = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
raw_data['day_name'] = raw_data['day_of_week'].map(day_name_mapping)

# Sort the days of the week
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
raw_data['day_name'] = pd.Categorical(raw_data['day_name'], categories=days_order, ordered=True)

# Use a color palette from seaborn
sns.set_palette("pastel")

# Bar plot for Temporal Trends by Day of the Week with sorted day names
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")  # Add grid lines
raw_data.groupby('day_name')['SALES'].sum().sort_index().plot(kind='bar')

# Labels and titles
plt.title('SALES Over the Days of the Week', fontsize=16)
plt.xlabel('Day of the Week', fontsize=14)
plt.ylabel('SALES', fontsize=14)

# Legend
plt.legend(['SALES'], loc='upper right')

# Data labels
for index, value in enumerate(raw_data.groupby('day_name')['SALES'].sum().sort_index()):
    plt.text(index, value + 1, str(value), ha='center', va='bottom')

plt.grid(True)
plt.show()


# =============================================================================
# PART 3
# =============================================================================


# Adjust the number of top descriptions to show (e.g., top 10)
top_n = 10
top_descriptions = raw_data['PRODUCTCODE'].value_counts().nlargest(top_n).index

# Use a color palette from seaborn
sns.set_palette("pastel")

plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")  # Add grid lines

# Filter data for top PRODUCTCODE
filtered_data = raw_data[raw_data['PRODUCTCODE'].isin(top_descriptions)]

# Bar plot for sales by Top PRODUCTCODE
filtered_data.groupby('PRODUCTCODE')['SALES'].sum().plot(kind='bar')

# Labels and titles
plt.title('SALES by Top PRODUCTCODE', fontsize=16)
plt.xlabel('PRODUCTCODE', fontsize=14)
plt.ylabel('SALES', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Data labels
for index, value in enumerate(filtered_data.groupby('PRODUCTCODE')['SALES'].sum()):
    plt.text(index, value + 1, str(value), ha='center', va='bottom')

plt.show()

# =============================================================================
# PART 4
# =============================================================================

# Adjust the number of top descriptions to show (e.g., top 10)
top_n = 20
top_descriptions = raw_data['PRODUCTLINE'].value_counts().nlargest(top_n).index

# Use a color palette from seaborn
sns.set_palette("pastel")

plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")  # Add grid lines

# Filter data for top PRODUCTCODE
filtered_data = raw_data[raw_data['PRODUCTLINE'].isin(top_descriptions)]

# Bar plot for sales by Top PRODUCTCODE
filtered_data.groupby('PRODUCTLINE')['SALES'].sum().plot(kind='bar')

# Labels and titles
plt.title('SALES by Top PRODUCTLINE', fontsize=16)
plt.xlabel('PRODUCTLINE', fontsize=14)
plt.ylabel('SALES', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Data labels
for index, value in enumerate(filtered_data.groupby('PRODUCTLINE')['SALES'].sum()):
    plt.text(index, value + 1, str(value), ha='center', va='bottom')

plt.show()



















