import numpy as np

mid = []
final = []

while True:
    score = int(input())
    if score == -1:
        while True:
            f = int(input())
            if f == -1:
                break
            else:
                final.append(f)
        break
    else:
        mid.append(score)
        
first = []
sec = []
avg = []

for i in range(len(mid)):
    if i % 3 == 0:
        first.append([])
        sec.append([])
        avg.append([])

index = 0
for i in range(len(avg)):
    for j in range(3):
        first[i].append(mid[index])
        sec[i].append(final[index])
        index += 1

arr_m = np.array(first)
arr_f = np.array(sec)

aa = (arr_m + arr_f) / 2


for i in range(len(aa)):
    aa[i, 0] += 10

a = np.round(aa, 2)
a[a < 60] = -1

print(arr_m, arr_f, a, sep="\n\n")