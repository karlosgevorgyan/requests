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


user = 'https://ikrona.by/catalog/mebelnye_materialy/'

def material(headers, user_shatura):
    global session
    session = requests.Session ()
    global request
    request = session.get (user_shatura, headers=headers)
    if request.status_code == 200:
        print('ok')
    else:
        print('errror')


def materials_product():
    global soup
    soup = bs (request.content, 'html.parser')
    div = soup.find_all ('div', attrs={'class': 'catalog-section'})
    for divs in div:
        product_name = divs.find('span', attrs={'class': 'text-cont'}).text
        print(product_name)





def process():
    material (headers, user)
    materials_product ()

process()