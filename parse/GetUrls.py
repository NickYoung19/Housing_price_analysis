# 爬取所有城市的链接
from bs4 import BeautifulSoup
import requests
import json


city_urls = {}
url = 'https://www.lianjia.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')
soup.find_all('div', attrs={'class': 'city-enum fl'})
start = '大连租房'
end = '漳州'
flag = False
for s in soup:
    try:
        urls = s.find_all('a')
        for url in urls:
            if flag:
                city_name = url.string
                city_name = city_name.strip()
                link = url.get('href')
                city_urls[city_name] = link
            if url.string == start:
                flag = True
            elif url.string == end:
                flag = False
    except:
        continue


f = open('city_urls.json', 'w')
json.dump(city_urls, f)
f.close()
