# Housing-price-analysis
Realize the analysis of housing price in all parts of China.

开发工具：
    Python版本：3.6.4，Pycharm IDE

相关模块：
    openpyxl模块；requests模块；bs4模块；pyecharts模块；以及一些python自带的模块。

环境搭建：
    安装Python并添加到环境变量，pip安装需要的相关模块即可。

原理简介
需求：

    根据输入的城市名获取该城市的房价信息；

    对获得的数据进行简单的分析。

目标网站：

    链家网（https://dl.lianjia.com/）

实现思路：

    很基础的爬虫，不需要任何分析。直接请求需要的网页地址，然后利用bs4模块解析请求返回的数据并获取所需的信息即可。

    然后再对这些信息进行简单的分析。

    其中信息保存到Excel中，分析时读取即可。

    具体实现细节详见相关文件中的源代码。

数据爬取演示方法：
    在terminal窗口运行Spider.py文件后根据提示输入相关的信息即可。
