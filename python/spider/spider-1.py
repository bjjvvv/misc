import requests
from bs4 import BeautifulSoup

__author__ = 'bjj'

def trade_spider(max_pages):
    """just a function for finding all the images in the post
    """
    page = 1
    while page <= max_pages:
        url = 'http://photo.weibo.com/1191220232/talbum/index#!/mode/1/page/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        links = []
        for link in soup.findAll('img', {'class':'BDE_Image'}):
            links.append(link.get('src'))
        page += 1
    return links

if __name__ == '__main__':
    print("start")
    links = trade_spider(1)
    for link in links:
        print(link)