#! /Users/mabelfan/anaconda3/bin/python3
# lucky.py - Opens several Baidu search results

import requests, sys, webbrowser, bs4
from urllib.parse import urlencode, quote

print('百度中...')   # display text while downloading the Baidu page
# 如何找到百度搜索结果页面的path？已解决
keyword = ' '.join(sys.argv[1:])
# url = 'https://www.baidu.com/s?wd=' + quote(keyword)
# webbrowser.open(url)   # 验证可以打开百度搜索的结果页面

headersParameters = {    #发送HTTP请求时的HEAD信息，用于伪装为浏览器
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

res = requests.get('https://www.baidu.com/s?wd=' + quote(keyword), headers = headersParameters)
res.raise_for_status
# print(res)   # 得到<Response [200]>表示获取成功
# print(type(res))   # <class 'requests.models.Response'>
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(soup.title)  # 验证是否soup成功

linkElems = soup.select('.t a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
	print(linkElems[i].get('href'))
	webbrowser.open(linkElems[i].get('href'))
