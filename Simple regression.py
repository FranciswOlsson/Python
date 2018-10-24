#Linear Model
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np


#Let's load some data
url = 'https://raw.github.com/neurospin/pystatsml/master/datasets/salary_table.csv'
salary = pd.read_csv(url)

#EDA
salary.head()


y, x = salary.salary, salary.experience
beta, beta0, r_value, p_value, std_err = stats.linregress(x,y)
#print linear regression equation, r^2, 
print("y = %f x + %f, r: %f, r-squared: %f,\np-value: %f, std_err: %f"
% (beta, beta0, r_value, r_value**2, p_value, std_err))

#y = 491.486913 x + 13584.043803, r: 0.538886, r-squared: 0.290398, p-value: 0.000112, std_err: 115.823381

print("Regression line with the scatterplot")
yhat = beta * x + beta0 # regression line
plt.plot(x, yhat, 'r-', x, y,'o')
plt.xlabel('Experience (years)')
plt.ylabel('Salary')
plt.show()


print("Using seaborn")
import seaborn as sns
sns.regplot(x="experience", y="salary", data=salary);

