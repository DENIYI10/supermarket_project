**Supermarket Delta Data Analysis**

This project is about analyzing the sales data of Supermarket Delta in order to provide insights and visualizations for better decision making. The data is imported from a CSV file using the pandas library.

**Data Preparation**

Categorical variables in the dataset are converted to numerical variables using the LabelEncoder from the scikit-learn library. Date and Time columns are also converted into datetime format for better visualization. A function is defined to fetch the day, month, and year attributes of the Date column, and the resulting series is added to the sales dataframe. Similarly, the hour attribute of the Time column is extracted and added as a new column in the sales dataframe.

**Data Summarization**

The descriptive statistics of the sales dataframe are generated using the describe method of the pandas library. The missing data can also be viewed using the info method. The count of gender is obtained using the value_counts method. The gross income of each city is obtained by grouping the sales dataframe by City and computing the median gross income. The mean of the rating column is also calculated.

**Data Visualization**

The seaborn and matplotlib libraries are used for data visualization. Several functions are defined to generate count plots, box plots, line plots, scatter plots, bar plots, and pie charts. These functions are used to visualize the sales data in various ways. Some of the visualizations include:

    Gender count plot
    Bar plot of gross income against city
    Distribution plot of ratings with the average rating marked
    Bar plot of gross income against product line
    Bar plot of ratings against product line
    Count plot of quantities bought by customers
    Box plot of ratings against branch
    Line plot of customer type against hour
    Line plot of quantity against day with different colors for each month
    Line plot of customer type against day with different colors for each month
    Line plot of customer type against hour with different colors for each month
    Line plot of total sales against day with different colors for each month
    Count plot of products sold
    Count plot of payment method

All of the visualizations are generated using the sales dataframe and provide insights into the sales trends and patterns of Supermarket Delta.

**Conclusion**

The Supermarket Delta Data Analysis project uses the pandas, scikit-learn, seaborn, and matplotlib libraries to analyze the sales data of Supermarket Delta. The data is prepared, summarized, and visualized to provide insights into the sales trends and patterns. The visualizations can be used by Supermarket Delta to make better decisions and improve their sales.
