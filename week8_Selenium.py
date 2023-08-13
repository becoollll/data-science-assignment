from selenium import webdriver
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup

county = str(input())

################# chromedriver #################
chrome_options = Options()
chrome_options.add_argument("--headless")
path = "./chromedriver"
browser = webdriver.Chrome(executable_path = path, options=chrome_options)

def printt(city):

    browser.get("https://www.cwb.gov.tw/V8/E/W/County/County.html?CID=63")
    x = browser.find_element("id", 'CID')
    drop=Select(x)
    drop.select_by_visible_text(city)

    temp = browser.find_element("xpath", "/html/body/div[2]/main/div/div[1]/div[3]/div[2]/ul/li[1]/span[2]/span[1]")
    low = temp.text.split(" - ")[0]
    high = temp.text.split(" - ")[1]

    return(low, high)

if county != "all":
    temperature = printt(county)
    print(county)
    print(temperature[0],"-",temperature[1])
else:
    cities = ["Keelung City", "Taipei City", "New Taipei City",
              "Taoyuan City", "Hsinchu City", "Hsinchu County",
              "Miaoli County", "Taichung City", "Changhua County",
              "Nantou County", "Yunlin County", "Chiayi City",
              "Chiayi County", "Tainan City", "Kaohsiung City",
              "Pingtung County", "Yilan County", "Hualien County",
              "Taitung County", "Penghu County", "Kinmen County",
              "Lienchiang County"]
    tem = []
    for cnc in cities:
        temperature = printt(cnc)
        tem.append(temperature[0] + "-" + temperature[1])
    for i in range(len(cities)):
        print(cities[i], tem[i], sep="\n")