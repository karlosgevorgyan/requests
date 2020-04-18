import requests
from bs4 import BeautifulSoup as bs
import mysql.connector

mydata = mysql.connector.connect (
    host='localhost',
    user='root',
    passwd='1111',
    db='hh'
)

mycursor = mydata.cursor ()

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}

user = 'https://hh.ru/search/vacancy?area=1&st=searchVacancy&text=Python&from=suggest_post'


def scrap(headers, user):
    global company, meta_info, price, href, title, query
    session = requests.Session ()
    reques = session.get (user, headers=headers)
    if reques.status_code == 200:
        soup = bs(reques.content, 'html.parser')
        divs = soup.find_all ('div', attrs={'data-qa': 'vacancy-serp__vacancy'})

        for div in divs:
            title = div.find ('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
            href = div.find('a',attrs={'data-qa':'vacancy-serp__vacancy-title'})['href']
            company = div.find ('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text
            meta_info = div.find ('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text
            price = div.find ('div', attrs={'class': 'vacancy-serp-item__sidebar'}).text.strip ()

            list = [title,href,company,meta_info,price]
            for i in range(len(list)):
                print()
            query = """insert into info (title,href,company,meta_info,price) values (%s,%s,%s,%s,%s)"""
            mycursor.execute (query,list)
            mydata.commit ()

    else:
        print ('error')

scrap (headers, user)


