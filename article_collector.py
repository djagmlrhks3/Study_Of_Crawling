import os, codecs, re, datetime, requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

os.chdir(r'C:\Users\HeeKwan\Desktop\Crawling')

url = 'https://news.daum.net/'
f = open(str(datetime.date.today()) + 'articles.txt', 'w')

soup = bs(ur.urlopen(url).read(), 'html.parser')

for d in soup.find_all('div', {"class" : "thumb_relate"}):
    try:
        f.write(d.text + '\n')
        f.write(d.find_all('a')[0].get('href') + '\n')
        soup2 = bs(ur.urlopen(d.find_all('a')[0].get('href')).read(), 'html.parser')
        for p in soup2.find_all('p'):
            f.write(p.text)
    except:
        pass
    
f.close()