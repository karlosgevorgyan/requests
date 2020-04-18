import requests
from bs4 import BeautifulSoup as bs
import mysql.connector

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


user_shatura = 'http://www.shatura-mebel.com/goods/dante-bedroom'
def spalnya_process(headers, user_shatura):
    global session
    session = requests.Session ()
    global request
    request = session.get (user_shatura, headers=headers)
    if request.status_code == 200:
        print('ok')
    else:
        print('errror')

def spalnya():
    global soup
    soup = bs (request.content, 'html.parser')
    div = soup.find_all ('span', attrs={'class': 'element'})
    for divs in div:
        product_name = divs.find ('a', attrs={'class': 'element_prod_link'}).text
        product_image = divs.find ('div', attrs={'class': 'element_pic'})['style'][20:].strip (" ( ' ' ) ; ")
        product_price = divs.find ('strong').text
        product_size = divs.find ('div', attrs={'class': 'element_size'}).text
        product_code = divs.find ('div', attrs={'class': 'element_code'}).text
        print (
            'product_name' + ' - ' + product_name + ' - ' + 'product_image' + ' - ' + product_image + ' - ' + 'product_price' + ' - ' +
            product_price + ' - ' + 'product_size' + ' - ' + product_size + ' - ' + 'product_code' + ' - ' + product_code)

        list = [product_image]
        for i in range (len (list)):
            query = """insert into images (name) values (%s)"""
        mycursor.execute (query, list)
        mydata.commit ()


user_mebelvia = 'https://mebelvia.ru/katalog/korpusnaya_mebel/spalnie_garnitury/'
def spalnya_1():
    session = requests.Session ()
    request = session.get (user_mebelvia, headers=headers)
    soup = bs (request.content, 'html.parser')
    div = soup.find_all ('article', attrs={'class': 'catalog_item catalog_item-with-subimage lazy_load'})

    for divs in div:
        article_name = divs.find ('div', attrs={'class': 'catalog_item-description'}).text.strip ('\n')
        article_image = divs.find ('img')['big-src']
        article_prices = divs.find ('div', attrs={'class': 'catalog_item-bottom_price'})
        article_price = article_prices.find ('div', attrs={'class': 'catalog_item-bottom_price_current'}).text
        print ('article_name --    ' + article_name + '  ' +
               'article_price --   ' + article_price + '  ' +
               'article_image --   ' + article_image)


        list = [article_image]
        for i in range (len (list)):
            query = """insert into images (name) values (%s)"""
        mycursor.execute (query, list)
        mydata.commit ()


user_magazinmebeli = 'https://magazinmebeli.net/109-krovati-v-sovremennom-stile'
def spalnya_2():
    session = requests.Session ()
    request = session.get (user_magazinmebeli, headers=headers)

    soup = bs (request.content, 'html.parser')
    div = soup.find_all ('div', attrs={'class': 'product-container'})
    for divs in div:
        products_name = divs.find ('span', attrs={'class': 'product-name'}).text
        products_price = divs.find ('span', attrs={'class': 'price product-price'}).text
        products_href = divs.find ('a', attrs={'class': 'product_img_link'})['href']
        products_img = divs.find ('img')['src']

        print (products_name + ' --> ' + products_price + ' --> ' + products_href + ' --> ' + products_img)
        list = [products_img]
        for i in range (len (list)):
            query = """insert into images (name) values (%s)"""
        mycursor.execute (query, list)
        mydata.commit ()

# def cretae_url(url_path='',url_base=''):
#     if url_path.startswith ('http'):
#         return url_path
#     elif url_path.startswith ('//'):
#         return 'http' + url_path
#     elif url_base + url_path:
#         return
#     else:
#         return url_base + '/' + url_path


def process():
    spalnya_process (headers, user_shatura)
    spalnya()
    spalnya_1()
    spalnya_2()
    #cretae_url()
process()



# list = [products_name, products_price, products_href, products_img]
# for i in range (len (list)):
#     print ()
# query = """insert into product (product_name,product_price,product_href,product_image) values (%s,%s,%s,%s)"""
# mycursor.execute (query, list)
# mydata.commit ()