import requests
from bs4 import BeautifulSoup as bs
import mysql.connector


mydata = mysql.connector.connect (
    host='localhost',
    user='root',
    passwd='1111',
    db='Asko'
)

mycursor = mydata.cursor ()


headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}

user = 'https://asko.ua/okna/aluplast-gmbh'
def lusamut_dur(headers, user):
    session = requests.session ()
    reques = session.get (user, headers=headers)
    if reques.status_code == 200:
        soup = bs (reques.content, 'html.parser')
        divs = soup.find_all ('div', attrs={'class': 'product-layout col-lg-4 col-md-6 col-sm-6 col-sx-12'})
        for div in divs:
            product_name = div.find ('div', attrs={'class': 'product-name'}).text.strip ('\n')
            product_price = div.find ('div', attrs={'class': 'product-price'}).text.strip ('\n')
            product_img = div.find ('img')['src']
            product_href = div.find ('a')['href']
            print ('product__name --    ' + product_name + '  ' +
                   'product_price --    ' + product_price + '  ' +
                   'product_img   --    ' + product_img + '  ' +
                   'product__href --    ' + product_href)
            list = [product_name, product_price, product_img, product_href]
            for i in range (len (list)):
                print ()
            query = """insert into products_WINDOW_DOOR (product_name,product_price,product_img,product_href) values (%s,%s,%s,%s)"""
            mycursor.execute (query, list)
            mydata.commit ()


    else:
        print ('Error')

lusamut_dur (headers, user)

user_2 = 'https://asko.ua/okna/wds'
def lusamut_dur(headers, user_2):
    session = requests.session ()
    reques = session.get (user_2, headers=headers)
    if reques.status_code == 200:
        soup = bs (reques.content, 'html.parser')
        tables = soup.find_all ('div', attrs={'class': 'product-layout col-lg-4 col-md-6 col-sm-6 col-sx-12'})
        for table in tables:
            product_name = table.find ('div', attrs={'class': 'product-name'}).text.strip ('\n')
            product_price = table.find ('div', attrs={'class': 'product-price'}).text.strip ('\n')
            product_img = table.find ('img')['src']
            product_href = table.find ('a')['href']
            print (product_price)

            list = [product_name, product_price, product_img, product_href]
            for i in range (len (list)):
                print ()
            query = """insert into products_WINDOW_DOOR (product_name,product_price,product_img,product_href) values (%s,%s,%s,%s)"""
            mycursor.execute (query, list)
            mydata.commit ()


    else:
        print('error')
lusamut_dur(headers, user_2)
#
# user_door = 'https://asko.ua/dveri/vhodnye-dveri/irondoos'
# def doors(headers, user_door):
#     session = requests.session ()
#     reques = session.get (user_door, headers=headers)
#     if reques.status_code == 200:
#         soup = bs (reques.content, 'html.parser')
#         divs = soup.find_all ('div', attrs={'class': 'product-layout col-lg-4 col-md-6 col-sm-6 col-sx-12'})
#         for div in divs:
#             product_name = div.find ('div', attrs={'class': 'product-name'}).text.strip ('\n')
#             product_price = div.find ('div', attrs={'class': 'product-price'}).text.strip ('\n')
#             product_img = div.find ('img')['src']
#             product_href = div.find ('a')['href']
#             print ('product__name --    ' + product_name + '  ' +
#                    'product_price --    ' + product_price + '  ' +
#                    'product_img   --    ' + product_img + '  ' +
#                    'product__href --    ' + product_href)
#             list = [product_name, product_price, product_img, product_href]
#             for i in range (len (list)):
#                 print ()
#             query = """insert into products_WINDOW_DOOR (product_name,product_price,product_img,product_href) values (%s,%s,%s,%s)"""
#             mycursor.execute (query, list)
#             mydata.commit ()
#     else:
#         print ('Error')
#
# doors(headers, user_door)
#
# user_door_2 = 'https://asko.ua/dveri/vhodnye-dveri/medved'
# def doors(headers, user_door_2):
#     session = requests.session ()
#     reques = session.get (user_door_2, headers=headers)
#     if reques.status_code == 200:
#         soup = bs (reques.content, 'html.parser')
#         divs = soup.find_all ('div', attrs={'class': 'product-layout col-lg-4 col-md-6 col-sm-6 col-sx-12'})
#         for div in divs:
#             product_name = div.find ('div', attrs={'class': 'product-name'}).text.strip ('\n')
#             product_price = div.find ('div', attrs={'class': 'product-price'}).text.strip ('\n')
#             product_img = div.find ('img')['src']
#             product_href = div.find ('a')['href']
#             # print ('product__name --    ' + product_name + '  ' +
#             #        'product_price --    ' + product_price + '  ' +
#             #        'product_img   --    ' + product_img + '  ' +
#             #        'product__href --    ' + product_href)
#             list = [product_name, product_price, product_img, product_href]
#             for i in range (len (list)):
#                 print ()
#             query = """insert into products_WINDOW_DOOR (product_name,product_price,product_img,product_href) values (%s,%s,%s,%s)"""
#             mycursor.execute (query, list)
#             mydata.commit ()
#     else:
#         print ('Error')
#
# doors(headers, user_door_2)


#
# user_ARCHES = 'https://asko.ua/dveri/arki'
# def arka(headers, user_ARCHES):
#     session = requests.session ()
#     reques = session.get (user_ARCHES, headers=headers)
#     if reques.status_code == 200:
#         soup = bs (reques.content, 'html.parser')
#         divs = soup.find_all ('div', attrs={'class': 'product-layout col-lg-4 col-md-6 col-sm-6 col-sx-12'})
#         for div in divs:
#             product_name = div.find ('div', attrs={'class': 'product-name'}).text.strip ('\n')
#             product_price = div.find ('div', attrs={'class': 'product-price'}).text.strip ('\n')
#             product_img = div.find ('img')['src']
#             product_href = div.find ('a')['href']
#
#             print ('product__name --    ' + product_name + '  ' +
#                    'product_price --    ' + product_price + '  ' +
#                    'product_img   --    ' + product_img + '  ' +
#                    'product__href --    ' + product_href)
#             print(product_name)
#
#             list = [product_name, product_price, product_img,product_href]
#             for i in range (len (list)):
#                 print ()
#             query = """insert into products_WINDOW_DOOR (product_name,product_price,product_img,product_href) values (%s,%s,%s,%s)"""
#             mycursor.execute (query, list)
#             mydata.commit ()
#     else:
#         print ('Error')
#
# arka(headers, user_ARCHES)
