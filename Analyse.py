# 分析
from openpyxl import load_workbook
from pyecharts import Bar
import random


wb = load_workbook('./results/北京.xlsx')
sheet = wb.active
main_price = []
second_price = []
for name, cell in zip(list(sheet.columns)[0], list(sheet.columns)[3]):
    try:
        name_ = name.value
        price = int(cell.value)
        main_price.append([name_, price])
    except:
        continue
for name, cell in zip(list(sheet.columns)[0], list(sheet.columns)[4]):
    try:
        name_ = name.value
        price = int(cell.value)
        second_price.append([name_, price])
    except:
        continue


def DrawBar(bar_name, price):
    bar = Bar(bar_name)
    attrs = []
    values = []
    for p in price:
        attrs.append(p[0])
        values.append(p[1])
    bar.add("房价(元/平方)", attrs, values, mark_point=["average", "min", "max"])
    bar.render('Bar{}.html'.format(random.random()))


if __name__ == '__main__':
    DrawBar('北京房价(元/平方)', main_price)
    DrawBar('北京房价(万元/套起)', second_price)
