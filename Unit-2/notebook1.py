import statistics as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('/home/vinoth/DataScience/datasets/diabetes.csv')

bp  = data['BloodPressure'].to_numpy()
gluc = data['Glucose'].to_numpy()
bmi = data['BMI'].to_numpy()
age = data['Age'].to_numpy()

plt.subplot(2,2,1)
sns.distplot(bp)
plt.title('Blood Pressure', fontsize = 15, loc='center')
plt.xlabel('BP', fontsize = 10)

plt.subplot(2,2,2)
sns.distplot(gluc)
plt.title('Glucose', fontsize = 15, loc='center')
plt.xlabel('Glucose', fontsize = 10)

plt.subplot(2,2,3)
sns.distplot(bmi)
plt.title('BMI', fontsize = 15, loc='center')
plt.xlabel('BMI', fontsize = 10)

plt.subplot(2,2,4)
sns.distplot(age)
plt.title('Age', fontsize = 15, loc='center')
plt.xlabel('Age', fontsize = 10)

plt.tight_layout()
plt.show()