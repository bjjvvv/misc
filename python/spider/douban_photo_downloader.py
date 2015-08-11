#! /usr/bin/python3
import requests
from lxml.cssselect import CSSSelector
from lxml import etree
from os.path import basename

"""指定下载豆瓣的相册
"""

import requests

#  r = requests.get('http://www.douban.com/photos/album/83687854/')
#
# with open('./source.html', 'wb') as f:
#     f.write(r.content)
#  
#  with open('./source.html', 'r') as f:
#      source = f.read()
#  
#  select = CSSSelector('a.photolst_photo')
#  html = etree.HTML(source)
#  links = [link.get('href') for link in select(html)]
#  print(*links, sep='\n')
#  print(len(links))
#  

def download_page_photos(link):
    'return next page link'
    r = requests.get(link)
    source = r.text
    select = CSSSelector('a.photolst_photo')
    html = etree.HTML(source)
    links = [link.get('href') for link in select(html)]
    for lk in links:
        img_url = get_img_url(lk)
        print('正在下载：' + img_url)
        r = requests.get(img_url)
        print(r.headers['content-length'])
        with open('./地铁/' + basename(img_url), 'wb') as f:
            f.write(r.content)
    return next_page(html)

def get_img_url(link):
    r = requests.get(link)
    html = etree.HTML(r.text)
    select_img = CSSSelector('div.link-report img')
    select_large_img = CSSSelector('#pic-viewer img')
    select_large_link = CSSSelector('div.report-link a')

    large_link_elms = select_large_link(html)
    if len(large_link_elms) > 0:
        link = large_link_elms[0].get('href')
        r = requests.get(link)
        html = etree.HTML(r.text)
        return select_large_img(html)[0].get('src')
    else:
        return select_img(html)[0].get('src')


def next_page(html):
    select = CSSSelector('span.next a')
    next_link_elm = select(html)
    return next_link_elm[0].get('href') if len(next_link_elm) > 0 else None
#  print(next_page(html))
#  for lk in links:
#      print(get_img_url(lk))
def start(url):
    next_page = url
    i = 0
    while(next_page is not None):
        i += 1
        print('正在下载第{}页====================='.format(i))
        next_page = download_page_photos(next_page)
if __name__ == '__main__':
    start('http://www.douban.com/photos/album/83687854/')
    
