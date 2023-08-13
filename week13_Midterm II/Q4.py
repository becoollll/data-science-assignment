import pandas as pd

df = pd.read_csv('Taiwan_city.csv')
temp = ''
cities = []

for i in df.index:
    if(temp!=df.iloc[i].City):
        cities.append(df.iloc[i].City)
        temp = df.iloc[i].City

data = df.values.tolist()
P = []
Area = []
Den = []

for i in range(len(cities)):
    P.append(0)
    Area.append(0)
    Den.append(0)

for d in data:
    for i in range(len(cities)):
        if d[0] == cities[i]:
            P[i] += d[2] + d[3]
            Area[i] += d[4]

for i in range(len(P)):
    Den[i] = P[i]/Area[i]

arr = []

for i in range(len(cities)):
    arr.append([])
    arr[i].append(cities[i])
    arr[i].append(P[i])
    arr[i].append(Area[i])
    arr[i].append(Den[i])

col = ["City", "Population", "Area", "Density"]
dff = pd.DataFrame(arr, columns = col)
dff.sort_values(["Density"], ascending=False, inplace=True, ignore_index=True)
dff.head()