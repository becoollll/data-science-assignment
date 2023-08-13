from bs4 import BeautifulSoup
import requests

res = requests.get('https://rate.bot.com.tw/xrt?Lang=en-US')
soup = BeautifulSoup(res.text, 'html.parser')
cur_temp = soup.select('div.hidden-phone')
rate_temp = soup.select('td.rate-content-cash.text-right.print_hide')

in_cur = str(input())
in_twd = eval(input())

ans = 0
sell = []
cur=[]
temp = 0

for i in range(1, 38, 2):
    if rate_temp[i].text != "-":
        sell.append(float(rate_temp[i].text))
    else:
        sell.append("-")

for i in range(len(cur_temp)):
    if in_cur == cur_temp[i].text.split("(")[1].split(")")[0]:
        temp = in_cur
        if sell[i] != "-":
            ans = in_twd / sell[i]
            print(format(ans, '.3f'), temp)
        else:
            print(f"{temp} doesn't have sell rate.")