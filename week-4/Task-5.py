# Task 5: Matplotlib Visualization
# Using a suitable dataset, create the following visualizations:
# 1. Line Chart
# 2. Bar Chart
# 3. Pie Chart
# 4. Histogram
# 5. Scatter Plot
#
# For each visualization:
# 1. Add an appropriate title.
# 2. Label the axes where applicable.
# 3. Use meaningful data.
# 4. Write a brief explanation.

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 180, 160, 220]

products = ["Coffee", "Tea", "Juice", "Milk"]
product_sales = [120, 90, 60, 80]

advertising = [10, 20, 30, 40, 50]
revenue = [100, 180, 250, 310, 400]

plt.figure(figsize=(7, 5))
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

print("Line Chart: Shows how sales change over the months.")

plt.figure(figsize=(7, 5))
plt.bar(products, product_sales)
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.show()

print("Bar Chart: Compares the sales of different products.")

plt.figure(figsize=(7, 5))
plt.pie(product_sales, labels=products, autopct="%1.1f%%")
plt.title("Product Sales Distribution")
plt.tight_layout()
plt.show()

print("Pie Chart: Shows each product's percentage of total sales.")

plt.figure(figsize=(7, 5))
plt.hist(sales, bins=5, edgecolor="black")
plt.title("Distribution of Monthly Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

print("Histogram: Shows the frequency distribution of sales values.")

plt.figure(figsize=(7, 5))
plt.scatter(advertising, revenue)
plt.title("Advertising vs Revenue")
plt.xlabel("Advertising Expenditure")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

print("Scatter Plot: Shows the relationship between advertising and revenue.")
