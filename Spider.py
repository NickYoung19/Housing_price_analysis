# 爬取链家网房价数据
# 作者: Nick Peng
import json
from openpyxl import Workbook
import requests
from bs4 import BeautifulSoup
import os
import time
import random


f = open('./parse/city_urls.json', 'r')
data = json.load(f)


# 将数据保存到Excel
def save_to_excel(infos, excel_name='loupan'):
    print('[INFO]:Start to save data...')
    wb = Workbook()
    ws = wb.active
    ws.append(['楼盘', '地点', '状态', '元/平(均价)', '总价(万/套起)', '建面(m^2)'])
    for info in infos:
        try:
            ws.append([info[0], info[1], info[2], info[3], info[4], info[5]])
        except:
            print('[WARNING]:One lost...')
            continue
    if not os.path.exists('./results'):
        os.mkdir('./results')
    wb.save('./results/' + excel_name + '.xlsx')
    print('[INFO]:Data saved to excel successfully...')


# 爬取信息
def GetInfo(url, page_num=10):
    print('[INFO]:Start to get infos...')
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
    infos = []
    for i in range(page_num):
        url = url + 'pg{}/'.format(i+1)
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'lxml')
        resblocks = soup.find_all('div', attrs={'class': 'resblock-name'})
        resblocks_area = soup.find_all('div', attrs={'class': 'resblock-area'})
        resblocks_location = soup.find_all('div', attrs={'class': 'resblock-location'})
        resblocks_price = soup.find_all('div', attrs={'class': 'resblock-price'})
        assert len(resblocks) == len(resblocks_area); assert len(resblocks) == len(resblocks_location); assert len(resblocks) == len(resblocks_price)
        info_num = len(resblocks)
        for i in range(info_num):
            resblock_price = resblocks_price[i]
            if resblock_price.find('span', attrs={'class': 'desc'}).string.strip() == '万/套(均价)':
                main_price = '暂无'
            else:
                main_price = resblock_price.find('span', attrs={'class': 'number'}).string.strip()
            second_price = resblock_price.find('div', attrs={'class': 'second'}).string.strip('总价万/套起')
            resblock_location = resblocks_location[i]
            location = resblock_location.find('a').string.strip()
            resblock_area = resblocks_area[i]
            area = resblock_area.find('span').string.strip().split(' ')[1][:-2]
            resblock = resblocks[i]
            resblock_name = resblock.find('a').string.strip()
            resblock_type = resblock.find('span', attrs={'class': 'resblock-type'}).string.strip()
            resblock_status = resblock.find('span', attrs={'class': 'sale-status'}).string.strip()
            infos.append([resblock_name, location, resblock_type+'-'+resblock_status, main_price, second_price, area])
        time.sleep(random.random() * 2)
    return infos


# main fun.
def main():
    city_name = input('Input the city name you want to know:')
    page_num = input('Input the page num you want to get:')
    try:
        city_url = data[city_name] + '/loupan/'
    except:
        print('[Error]: City name parse error...')
        return
    try:
        page_num = int(page_num)
    except:
        print('[Error]: Page number should be number...')
        return
    infos = GetInfo(city_url, page_num)
    save_to_excel(infos, excel_name=city_name)




if __name__ == '__main__':
    while True:
        main()