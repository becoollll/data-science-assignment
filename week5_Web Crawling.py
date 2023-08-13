from bs4 import BeautifulSoup
import pandas as pd
import requests

res = requests.get('https://sys.ndhu.edu.tw/SA/XSL_ApplyRWD/ActApply.aspx?lang=en')
soup = BeautifulSoup(res.text, 'html.parser')

name = []
hour = []
num = []
reg = []
time = []

for i in range(10):
    name.append(soup.find("span", {"id": f"BodyContent_gvActs_lblGv_act_name_{i}"}).text)
    hour.append(soup.find("span", {"id": f"BodyContent_gvActs_lblGv_xsl_check_{i}"}).text.split(" ")[2])
    num.append(soup.find("span", {"id": f"BodyContent_gvActs_lblGv_reg_num_{i}"}).text.split(" ")[0])
    reg.append(soup.find("span", {"id": f"BodyContent_gvActs_lblGv_reg_dt_{i}"}).text)
    time.append(soup.find("span", {"id": f"BodyContent_gvActs_lblGv_act_dt_{i}"}).text)

for i in range(10):
    print(name[i], hour[i], num[i], reg[i], time[i])

df = pd.DataFrame(list(zip(name, hour, num, reg, time)), columns =['Name of the activity', 'Number of hours certified', "Number of people who have registered", "Date and time of registeration", "Date and time of the activity"]) 

df