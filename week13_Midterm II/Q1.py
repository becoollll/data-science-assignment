# A-D 10%, E-G 20%
# H-N
# O-U
# V-AE rollcall 0, 1 每次佔10%
# Final = 各0.3 + 點名0.3

import pandas as pd
import numpy as np

df = pd.read_csv('data_q1.csv')
temp_d = df.values.tolist()

#column name to stu1
one = list(df.columns)
for i in range(len(one)):
    one[i] = int(float(one[i]))
data = []
data.append(one)
for d in temp_d:
    data.append(d)

col = ['A', 'B', 'C', 'D', 'E',
   'F', 'G', 'H', 'I', 'J',
   'K', 'L', 'M', 'N', 'O',
   'P', 'Q', 'R', 'S', 'T',
   'U', 'V', 'W', 'X', 'Y',
   'Z', 'AA', 'AB', 'AC', 'AD', 'AE']
idx = ["1","2","3","4","5","6","7","8","9","10"]
dff = pd.DataFrame(data, columns=col, index=idx)
score = []

for i in range(len(data)):
    score.append([])
    score[i].append(0)
    score[i].append(0)
    score[i].append(0)
    score[i].append(0)

for i in range(len(dff)):
    first=0
    sec = 0
    third = 0
    roll = 0
    final = 0
    for j in range(4):
        first += dff.loc[idx[i]][col[j]] * 0.1
        sec += dff.loc[idx[i]][col[j+7]] * 0.1
        third += dff.loc[idx[i]][col[j+14]] * 0.1
    for j in range(4, 7):
        first += dff.loc[idx[i]][col[j]] * 0.2
        sec += dff.loc[idx[i]][col[j+7]] * 0.2
        third += dff.loc[idx[i]][col[j+14]] * 0.2
    score[i][0] += first
    score[i][1] += sec
    score[i][2] += third
    for j in range(21, 31):
        roll += dff.loc[idx[i]][col[j]]
    final = first*0.3 + sec*0.3 + third *0.3 + roll*0.3
    if final > 100:
        final = 100
    score[i][3] = final

#四捨五入
for i in range(len(score)):
    for j in range(len(score[i])):
        if score[i][j] - int(score[i][j]) != 0:
            if score[i][j] - int(score[i][j]) >= 0.5 and score[i][j] - int(score[i][j]) < 1:
                score[i][j] += 1-(score[i][j] - int(score[i][j]))
            elif score[i][j] - int(score[i][j]) > 0 and score[i][j] - int(score[i][j]) < 0.5:
                score[i][j] -= 1-(score[i][j] - int(score[i][j]))

sco = np.array(score, dtype=int)
print(sco)
col_sco = ["first mid-term", "second mid-term", "third mid-term", "Total semester grade"]
dff = pd.DataFrame(sco, columns = col_sco)
dff.to_csv("410921217_Q1.csv", index = False)