from bs4 import BeautifulSoup
import requests

res = requests.get("https://www.taiwanlottery.com.tw/lotto/lotto649/history.aspx")
soup = BeautifulSoup(res.text, 'html.parser')

date = str(input())
num = str(input())

da = ['112000037', '112000036', '112000035', '112000034', '112000033', '112000032', '112000031', '112000030', '112000029', '112000028']
number = []

for i in range(len(da)):
    if date == da[i]:
        index = i

for i in range(1,7):
    number.append(soup.find("span", {"id":f"Lotto649Control_history_dlQuery_SNo{i}_{index}"}).text)
number.append(soup.find("span", {"id":f"Lotto649Control_history_dlQuery_No7_{index}"}).text)
num = num.split(", ")

for i in range(len(num)):
    if len(num[i]) < 2:
        num[i] = "0" + num[i]

count = 0
for i in range(6):
    for j in range(6):
        if num[i] == number[j]:
            count += 1

flag = 0
for i in range(len(num)):
    if num[i] == number[6]:
        flag = 1
        
if count == 6:
    print("Jackpot")
elif count == 5:
    if flag == 1:
        print("Second prize")
    else:
        print("Third prize")
elif count == 4:
    if flag == 1:
        print("Fourth prize")
    else:
        print("Fifth prize")
elif count == 3:
    if flag == 1:
        print("Sixth prize")
    else:
        print("Eighth prize")
elif count == 2 and flag == 1:
    print("Seventh prize")
else:
    print("NO")