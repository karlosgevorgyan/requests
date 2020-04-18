import requests
from bs4 import BeautifulSoup as bs
import  mysql.connector


mydata = mysql.connector.connect (
    host='localhost',
    user='root',
    passwd='1111',
    db='wdf'
)

mycursor = mydata.cursor ()

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}


user_mebelvia = 'https://mebelvia.ru/katalog/kuhni_i_stolovye_gruppy/'

def kuxnya_process(headers, user_mebelvia):
    global session
    session = requests.Session ()
    global request
    request = session.get (user_mebelvia, headers=headers)
    if request.status_code == 200:
        print('ok')
    else:
        print('errror')


def kuxnya():
    global soup, query
    soup = bs (request.content, 'html.parser')
    div = soup.find_all ('article', attrs={'class': 'catalog_item catalog_item-with-subimage lazy_load'})
    for divs in div:
        article_name = divs.find ('div', attrs={'class': 'catalog_item-description'}).text.strip ('\n')
        article_prices = divs.find ('div', attrs={'class': 'catalog_item-bottom_price'})
        article_price = article_prices.find ('div', attrs={'class': 'catalog_item-bottom_price_current'}).text
        article_image = divs.find ('img')['big-src']

        print('article_name --    ' + article_name + '  ' +
               'article_price --   ' + article_price + '  ' +
               'article_image --   ' + article_image)

        list = [article_image]
        for i in range (len (list)):
            query = """insert into images (name) values (%s)"""
        mycursor.execute (query, list)
        mydata.commit ()




user_mebelvia_2_page = 'https://mebelvia.ru/katalog/kuhni_i_stolovye_gruppy/page-2/'

def kuxnya_2():
    session = requests.Session ()
    request = session.get (user_mebelvia_2_page, headers=headers)
    soup = bs (request.content, 'html.parser')
    div = soup.find_all ('article', attrs={'class': 'catalog_item catalog_item-with-subimage lazy_load'})
    for divs in div:
        article_name = divs.find ('div', attrs={'class': 'catalog_item-description'}).text.strip ('\n')
        article_prices = divs.find ('div', attrs={'class': 'catalog_item-bottom_price'})
        article_price = article_prices.find ('div', attrs={'class': 'catalog_item-bottom_price_current'}).text
        article_image = divs.find ('img')['big-src']

        print ('article_name --    ' + article_name + '  ' +
                'article_price --   ' + article_price + '  ' +
                'article_image --   ' + article_image)

        list = [article_image]
        for i in range (len (list)):
            query = """insert into images (name) values (%s)"""
        mycursor.execute (query, list)
        mydata.commit()


user_sovremennye = 'https://kuhni.mebelvia.ru/katalog/kuhni/sovremennye/'

def kuxnya_3():
    session = requests.Session ()
    request = session.get (user_sovremennye, headers=headers)
    soup = bs (request.content, 'html.parser')
    div = soup.find_all ('div', attrs={'class': 'knz-bck-12 knz-kitchenBck'})
    for divs in div:
        elemnet_name = divs.find ('a', attrs={'class': 'knz-new-tab'}).text.strip ('\n')
        elemnet_price = divs.find ('span', attrs={'class': 'knz-kitchenMainPrice'}).text.strip ('\n')
        elemnet_image = divs.find ('img')['src']

        print (elemnet_name)
        print ('   ')
        print (elemnet_price)
        print ('   ')
        print (elemnet_image)
        list = [elemnet_image]
        for i in range(len (list)):
            query = """insert into images (name) values (%s)"""
        mycursor.execute (query, list)
        mydata.commit ()



user_stolplit = 'https://www.stolplit.ru/internet-magazin/katalog-mebeli/24-kuxonnye-garnitury/'
def kuxnya_4():
     session = requests.Session ()
     request = session.get (user_stolplit, headers=headers)
     soup = bs(request.content, 'html.parser')
     table = soup.find_all ('div', attrs={'class': 'product product--category'})
     for tables in table:
         product__name = tables.find ('a', attrs={'class': 'js-product-link'}).text
         product__price = tables.find ('span', attrs={'class': 'price'}).text.strip ('\n')
         product__img = tables.find ('img')['src']
         product__href  = tables.find ('a')['href'].strip('/')
         print('product__name --    ' + product__name + '  ' +
               'product__img  --   ' + product__img + '  ' +
               'product__price --   ' + product__price + '  ' +
               'product__href --    ' + product__href)
         # list = [product__img]
         # for i in range (len (list)):
         #     query = """insert into images (name) values (%s)"""
         # mycursor.execute (query, list)
         # mydata.commit ()


def proccess():
    kuxnya_process(headers,user_mebelvia)
    kuxnya()
    kuxnya_2()
    #kuxnya_3() ??
    #kuxnya_4() ??
proccess()