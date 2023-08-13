import pandas as pd

df = pd.read_csv('US_Population_2021.csv')

child = 0 #0-14
youth = 0 #15-24
adult = 0 #25-64
old = 0 # 65up
data = df.values.tolist()
data[100][0] = "101"

for d in data:
    if int(d[0]) < 15:
        child += float(d[1].split('%')[0])*0.01
        child += float(d[2].split('%')[0])*0.01
    elif int(d[0]) < 25:
        youth += float(d[1].split('%')[0])*0.01
        youth += float(d[2].split('%')[0])*0.01
    elif int(d[0]) < 65:
        adult += float(d[1].split('%')[0])*0.01
        adult += float(d[2].split('%')[0])*0.01
    elif int(d[0]) >= 65:
        old += float(d[1].split('%')[0])*0.01
        old += float(d[2].split('%')[0])*0.01

c_f = child / (child + youth + adult + old) * 100
y_f = youth / (child + youth + adult + old) * 100
a_f = adult / (child + youth + adult + old) * 100
e_f = old / (child + youth + adult + old) * 100

print("Child population ratio (regardless of gender):", round(c_f, 2))
print("Youth population ratio (regardless of gender):", round(y_f, 2))
print("Adult population ratio (regardless of gender):", round(a_f, 2))
print("Elderly population ratio (regardless of gender):", round(e_f, 2))