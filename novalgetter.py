import  requests
import threading
from bs4 import BeautifulSoup
import re
import os
import time
req_header={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cookie':'UM_distinctid=164d00b49a32fa-0943b2a30b6158-16396952-13c680-164d00b49a49e; Hm_lvt_5ee23c2731c7127c7ad800272fdd85ba=1532498758,1533107537,1533107672; bcolor=; font=; size=; fontcolor=; width=; bookid=38%2C1; CNZZDATA1261736110=512588368-1532495157-https%253A%252F%252Fwww.google.com.hk%252F%7C1533192464; Hm_lpvt_5ee23c2731c7127c7ad800272fdd85ba=1533197165; chapterid=10605000%2C260824; chaptername=%25u7B2C%25u5341%25u4E09%25u7AE0%2520%25u7384%25u6C34%25u4E39%2520%25u4E09%2C%25u8BB8%25u7ACB%25u56FD%25u5916%25u4F20',
'Host':'www.qu.la',
'Proxy-Connection':'keep-alive',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
}
req_url_base='http://www.qu.la/book/'           #小说主地址
req_url=req_url_base+"38/"                       #单独一本小说地址
txt_section='29712.html'                  #某一章页面地址

#请求当前章节页面  params为请求参数
r=requests.get(req_url+str(txt_section))
#soup转换
soup=BeautifulSoup(r.text,"html.parser")
print(soup.select('#wrapper'))
section_name=soup.select('#wrapper .content_read .box_con .bookname h1')[0].text
print('章节名:'+section_name)
#获取章节文本
section_text=soup.select('#wrapper .content_read .box_con #content')[0]
for ss in section_text.select("script"):                #删除无用项
    ss.decompose()
#按照指定格式替换章节内容，运用正则表达式
section_text=re.sub( '\s+', '\r\n\t', section_text.text).strip('\r\n')
txt_section=soup.select('#wrapper .content_read .box_con .bottem1 #pager_next')[0]['href']
print(txt_section)

print("章节内容：\n"+section_text)