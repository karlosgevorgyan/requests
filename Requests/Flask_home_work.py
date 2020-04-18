import requests
from bs4 import BeautifulSoup as bs
import csv

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}

user = 'https://www.books.am/am/--9804.html'

def book(headers, user):
    global soup
    session = requests.session ()
    global reques
    reques = session.get (user, headers=headers)
    soup = bs (reques.content, 'html.parser')
    divs = soup.find_all ('div', attrs={'class': 'product_block'})

    for div in divs:
        book_name = div.find('div',attrs={'class':'product_name_author fl'}).text
        book_info = div.find ('table', attrs={'class': 'product_details fl'}).text.strip()
        print(book_name + '\n' +  book_info)
        list = [book_name,book_info]

    with open('text.csv', 'w') as file:
        csv.writer(file)
        for row in list:
            file.write(row)



user2 = 'https://www.books.am/am/2-222285.html'

def book_2():
    session = requests.Session ()
    request = session.get (user2, headers=headers)
    soup = bs (request.content, 'html.parser')
    divs = soup.find_all ('div', attrs={'class': 'product_block'})
    for div in divs:
        book_name = div.find ('div', attrs={'class': 'product_name_author fl'}).text
        book_info = div.find ('table', attrs={'class': 'product_details fl'}).text.strip ()
        print (book_name + '\n' + book_info)
        list = [book_name, book_info]

    with open ('../applicetion22/templates/text1.csv', 'w') as file:
        csv.writer (file)
        for row in list:
            file.write (row)


user2 = 'https://www.books.am/am/1-35000491.html'

def book_3():
    session = requests.Session ()
    request = session.get (user2, headers=headers)
    soup = bs (request.content, 'html.parser')
    divs = soup.find_all ('div', attrs={'class': 'product_block'})
    for div in divs:
        book_name = div.find ('div', attrs={'class': 'product_name_author fl'}).text
        book_info = div.find ('table', attrs={'class': 'product_details fl'}).text.strip ()
        print (book_name + '\n' + book_info)
        list = [book_name, book_info]

    with open ('text2.csv', 'w') as file:
        csv.writer (file)
        for row in list:
            file.write (row)

def process():
    book_2()
    book(headers, user)
    book_3()
process()