import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('US_Population_2022.csv')
plt.figure(figsize=(16,16))
age = df['Age'].values.tolist()
age[100] = "101"

m = []
f = []

for a in age:
    m.append(float(a) - 0.2)
    f.append(float(a) + 0.2)

data = df.values.tolist()
sumM=0
sumF=0
data[100][0] = "101"

for d in data:
    sumM += d[1] * 0.01
    sumF += d[2] * 0.01

p = [sumM, sumF]
labels = ["Male", "Female"]

#1
plt.subplot(211)
plt.bar(m, df['Male % of Population'], label = "Male", width = 0.4)
plt.bar(f, df['Female % of Population'], label = "Female", width = 0.4)
plt.title("The bar chart of population",fontsize=24)
plt.xlabel("age", fontsize=18)
plt.ylabel("precentage of population", fontsize=18)
plt.legend(loc="upper right")
plt.xticks(np.arange(0,101,20))

#2
plt.subplot(212)
plt.pie(p, labels = labels, autopct="%1.1f%%")
plt.title("The pie chart of gender", fontsize=24)
plt.legend(loc="upper right")
plt.tight_layout()
plt.savefig("410921217_Q3.jpg")
plt.show()