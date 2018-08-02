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
'Cookie':'__cfduid=d577ccecf4016421b5e2375c5b446d74c1499765327; UM_distinctid=15d30fac6beb80-0bdcc291c89c17-9383666-13c680-15d30fac6bfa28; CNZZDATA1261736110=1277741675-1499763139-null%7C1499763139; tanwanhf_9821=1; Hm_lvt_5ee23c2731c7127c7ad800272fdd85ba=1499612614,1499672399,1499761334,1499765328; Hm_lpvt_5ee23c2731c7127c7ad800272fdd85ba=1499765328; tanwanpf_9817=1; bdshare_firstime=1499765328088',
'Host':'www.qu.la',
'Proxy-Connection':'keep-alive',
'Referer':'http://www.qu.la/book/1265/765108.html',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
}
req_url_base='http://www.qu.la/book/'           #小说主地址
req_url=req_url_base+"38/"                       #单独一本小说地址
txt_section='10604965.html'                  #某一章页面地址
res=requests.get(req_url,params=req_header)             #获取小说目录界面
soups=BeautifulSoup(res.text,"html.parser")
#请求当前章节页面
# r=requests.get(req_url+str(txt_section))
#soup转换
# soup=BeautifulSoup(r.text,"html.parser")
first_page=soups.select('#wrapper .box_con div#list dl dd a')

print(len(first_page))#获取章节名称
first_page = first_page[0]
print(first_page)
# section_name=soup.select('#wrapper .content_read .box_con .bookname h1')[0].text
# #获取章节文本
# section_text=soup.select('#wrapper .content_read .box_con #content')[0]
# for ss in section_text.select("script"):                #删除无用项
#     ss.decompose()
# #按照指定格式替换章节内容，运用正则表达式
# section_text=re.sub( '\s+', '\r\n\t', section_text.text).strip('\r\n')
#
# print('章节名:'+section_name)
# print("章节内容：\n"+section_text)