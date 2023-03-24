# Putting DataSet In DataFRAME
import pandas as pd
sales = pd.read_csv('Supermarket Delta Data Excel Document.csv', delimiter=',')
print(sales)
print('\n')


# Convert categorical variables to numerical variables
# Encode the customer_type column
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
sales['Customer type'] = encoder.fit_transform(sales['Customer type'])


# Changing Time and Date format for visualisation purpose
from pandas import to_datetime
sales['Date'] = to_datetime(sales['Date'])
sales['Time'] = to_datetime(sales['Time'])
print(sales['Date'])
print(sales['Time'])


def fetch_att(x):
    day = x.day
    month = x.month
    year = x.year
    return pd.Series([day, month, year])  # pd.series is to convert it to series TO STORE IN DATAFRAME


print(sales['Date'].apply(fetch_att))

sales[['day', 'month', 'year']] = sales['Date'].apply(fetch_att)  # To INSERT INTO DATAFRAME

print(sales['Time'].apply(lambda x: x.hour))

sales['hour'] = sales['Time'].apply(lambda x: x.hour)

print(sales.columns)



# Summarize the data. You can use the describe method of the DataFrame to generate descriptive statistics:
print(sales.describe())
print('\n')

# Missing Data
# print(df.info())


# Gender count
print(sales.Gender.value_counts())
print('\n')

# Code for printing a particular table off the Dataset
City = sales['City'].unique()
print('Code for printing a particular table off the Dataset:', City)
print('\n')



# City with more gross income
City = sales.groupby(['City'])['gross income'].median()
print('City with more gross income:', City)
print('\n')

# Mean of Rating
Rating = sales['Rating'].mean()
print('Mean of Rating:', Rating)
print('\n')

print(sales['Customer type'].count())

# VISUALIZATION
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def return_count_plot(column, hue_name=None):
    return sns.countplot(x=column, data=sales, hue=hue_name)


def return_boxplot(x_column, y_column):
    return sns.boxplot(x=x_column, y=y_column, data=sales)


def return_line_plot(x_column, y_column):
    return sns.lineplot(x=x_column, y=y_column, data=sales)


def return_rel_plot(x_col, y_col, col_name=None, row_name=None, rel_type=None, hue_name=None, style_name=None):
    return sns.relplot(x=x_col, y=y_col, col=col_name, row=row_name, kind=rel_type, hue=hue_name, style=style_name, data=sales)


def return_pie(labels, sizes):
    return plt.pie(sizes, labels=labels, radius=1.2, autopct='%0.01f%%', shadow=True, data=sales)


def return_bar_plot(x_column, y_column):
    return sns.barplot(x=x_column, y=y_column, data=sales)


# GENDER GRAPH
return_count_plot('Gender', hue_name=None)
plt.show()

return_bar_plot('gross income', 'City')
plt.show()

# RATING AND AVG RATING
sns.displot(sales['Rating'])
plt.axvline(x=np.mean(sales['Rating']), c='red', label='avg rating')
plt.title('Rating Sales in 2019')
plt.xlabel('RATINGS')
plt.ylabel('NUM OF CUSTOMERS')
plt.show()

# Product with most income/ sales
return_bar_plot('Product line', 'gross income')
plt.show()

# AVG rating of each product line
return_bar_plot('Product line', 'Rating')
plt.show()

# Quantities bought by one customer
return_count_plot('Quantity')
plt.show()

# Analysis of trend of sales
return_boxplot('Branch', 'Rating')
plt.show()

return_line_plot('hour', 'Customer type')
plt.show()

# How much sales occurs in each and every branch with respect to each and every month
return_rel_plot(x_col='day', y_col='Quantity', rel_type='line', hue_name='month', style_name='month')
plt.show()

# busiest day
return_rel_plot(x_col='day', y_col='Customer type', rel_type='line',  hue_name='month', style_name='month')
plt.show()

return_rel_plot(x_col='hour', y_col='Customer type', rel_type='line',  hue_name='month', style_name='month')
plt.show()


# Analysing BEST SALE MONTH
return_rel_plot(x_col='day', y_col='Total', rel_type='line', hue_name='month', style_name='month')
plt.show()

# Most bought product
return_count_plot('Product line', hue_name=None)
plt.show()


# How customers make payment in the business
return_count_plot('Payment')
plt.show()


