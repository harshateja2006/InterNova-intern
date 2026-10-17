# Task 3: Correlation & Probability Basics
# Correlation:
# 1. Select two numerical variables from a dataset.
# 2. Calculate their correlation.
# 3. Determine whether the relationship is positive, negative, or weak.
#
# Probability:
# 4. Create a simple real-world probability example.
# 5. Calculate the probability.
# 6. Display and explain the result.

import numpy as np

advertising = [10, 20, 30, 40, 50]
sales = [15, 25, 35, 45, 55]

correlation = np.corrcoef(advertising, sales)[0, 1]

print("Advertising Expenditure:", advertising)
print("Sales:", sales)
print("Correlation Coefficient:", round(correlation, 2))

if correlation > 0.5:
    print("Relationship: Positive")
elif correlation < -0.5:
    print("Relationship: Negative")
else:
    print("Relationship: Weak")

favorable_outcomes = 3
total_outcomes = 10

probability = favorable_outcomes / total_outcomes

print("\nFavorable Outcomes:", favorable_outcomes)
print("Total Outcomes:", total_outcomes)
print("Probability:", round(probability, 2))
print("Probability Percentage:", probability * 100, "%")

print("\nExplanation:")

print("\n1. Correlation:")
print("The correlation coefficient is 1.0, indicating a perfect")
print("positive relationship between advertising expenditure")
print("and sales in the given dataset. As advertising expenditure")
print("increases, sales also increase.")

print("\n2. Probability:")
print("The probability of a favorable outcome is 3/10 = 0.3.")
print("Therefore, the probability is 30%, meaning that there is")
print("a 30% chance of a favorable outcome.")
