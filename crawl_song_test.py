#! /Users/mabelfan/anaconda3/bin/python3

import requests, bs4, re

html_doc = """
<html>
<head><title>不将就</title></head>
<body id="auto-id-32Wirc1CGpW0ouk" class="auto-1528185663465-parent">
<div class="g-bd4 f-cb">
<div class="g-mn4">
<div class="g-mn4c">
<div class="n-cmt" id="comment-box" data-tid="R_SO_4_31654343" data-count="0">
<div id="auto-id-LRHUAXKoaTwgIaUN">
<div class="u-title u-title-1">...</div>
<div class="m-cmmt">
<div class="smmts j-flag" id="auto-id-06oFS9xyTtQMEMGd">
<h3 class="u-hd4">精彩评论</h3>
<<div class="head">
<a href="/user/home?id=105163794"><img src="http://p1.music.126.net/GZHMVyugB2acyLRG3OKMEQ==/109951163238063030.jpg?param=50y50"></a></div>
<div class="cntwrap">
<div class="">
<div class="cnt f-brk">
<a href="/user/home?id=105163794" class="s-fc7">皮皮蟹我们冲</a>
"：我真不知道排名第一的那个评论是怎么上去的！"
</div>
</div>
<div class="rp"><div class="time s-fc4">2016年2月24日</div><a data-id="123189837" data-type="like" href="javascript:void(0)"><i class="zan u-icn2 u-icn2-12"></i> (14.1万)</a><span class="sep">|</span><a href="javascript:void(0)" class="s-fc3" data-id="123189837" data-type="reply">回复</a></div></div>
<div id="243664851528185663461" class="itm" data-id="24366485"><div class="head">
<a href="/user/home?id=50808932">
<img src="http://p1.music.126.net/2EpJIgBTCW9n8uk4OGyvSQ==/7927478836479926.jpg?param=50y50"></a></div>
<div class="cntwrap">
<div class="">
<div class="cnt f-brk">
<a href="/user/home?id=50808932" class="s-fc7">SasakiLee</a>"：在2015年6月30日有一个叫老王的人，在一个节目里把这首歌唱给了他的前女友。本来应该是完全合拍的两个人轰轰烈烈的爱一场，跨过国家，跨过时间，但因为很多原因，老王和他的前女友没有互相折磨到白头，只能分隔在异国他乡，最后，不过将就。"</div></div>
<div class="rp"><div class="time s-fc4">2015年6月30日</div><a data-id="24366485" data-type="like" href="javascript:void(0)"><i class="zan u-icn2 u-icn2-12"></i> (40711)</a><span class="sep">|</span><a href="javascript:void(0)" class="s-fc3" data-id="24366485" data-type="reply">回复</a></div></div></div>
"""


soup = bs4.BeautifulSoup(html_doc, "html.parser")
# print(soup.title)

song_cmmt = soup.select('div[class="cnt f-brk"]')
num = len(song_cmmt)

pat2 = r'.*\"：(.*?)\"'

song_cmmt_id =soup.select('a[class="s-fc7"]')    #use CSS select
id_name = soup.select('div[class="cnt f-brk"] > a')

cmmt_ids = {}  # match the username to the ID.
comments = []  # collect all comments into a list
for i in range(num):
	cmmt_ids[(song_cmmt_id[i].get('href'))[14:]] = id_name[i].contents
	comments.append(re.compile(pat2).findall(song_cmmt[i].text))   # apply re to find the comments

print(cmmt_ids)
print(comments)

# print(soup.h3.string)
