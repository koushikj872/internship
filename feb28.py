import matplotlib.pyplot as plt
import numpy as np

# Sample data for charts
categories = ['North', 'South', 'East', 'West']
values = [120, 90, 75, 105]

# Bar chart: sales by region
plt.figure(figsize=(8, 5))
plt.bar(categories, values, color=['#4C72B0', '#55A868', '#C44E52', '#8172B3'])
plt.title('Quarterly Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales (in units)')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.close()

# Pie chart: share of total sales
plt.figure(figsize=(6, 6))
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140, colors=['#4C72B0', '#55A868', '#C44E52', '#8172B3'])
plt.title('Sales Share by Region')
plt.tight_layout()
plt.savefig('pie_chart.png')
plt.close()

# Histogram: distribution of individual daily sales
daily_sales = np.array([14, 12, 15, 9, 10, 11, 13, 18, 17, 14, 8, 16, 15, 10, 12, 13, 14, 18, 19, 16])
plt.figure(figsize=(8, 5))
plt.hist(daily_sales, bins=6, color='#4C72B0', edgecolor='black')
plt.title('Histogram of Daily Sales')
plt.xlabel('Units Sold per Day')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('histogram.png')
plt.close()

# Short data story
story = (
    'The charts show that the North region leads quarterly sales, followed by West. '
    'South and East have smaller shares, indicating opportunity for growth in those markets. '
    'The histogram reveals daily sales clustering around 12-16 units, with fewer days at the low and high ends. '
    'Overall, the data suggests a stable performance with a clear regional gap that can guide future sales strategy.'
)
print(story)
