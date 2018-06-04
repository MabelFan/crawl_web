#! /Users/mabelfan/anaconda3/bin/python3
# lucky.py - Opens several Baidu search results

import requests, sys, webbrowser, bs4

print('百度中...')   # display text while downloading the Baidu page
res = requests.get('https://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')

linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://baidu.com' + linkElems[i].get('href'))
