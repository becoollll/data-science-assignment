from bs4 import BeautifulSoup
import requests
import pandas as pd

res = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(res.text, 'html.parser')
title=[]
title_temp = soup.select('span.titleline')

for i in range(len(title_temp)):
    title.append(title_temp[i].text.split(' (')[0])

point = []
score_temp = soup.select('span.score')

for i in range(len(score_temp)):
    try:
        point.append(score_temp[i].text.split(" ")[0])
    except: #cannot find points
        point.append(None)

link = []
link_temp = soup.select('span.titleline')

for i in range(1, 59, 2):
    link.append(str(link_temp).split('href="')[i].split('">')[0])

ans=[]
ans.append(title)
ans.append(point)
ans.append(link)

print(ans)