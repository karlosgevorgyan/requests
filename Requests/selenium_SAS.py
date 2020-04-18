import mysql.connector
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
url_prefix = "https://www.sas.am"


def insert_products(products):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='1111',
        db='BASE'
    )
    cursor = conn.cursor()
    query = """insert into products (product_id, title, descriptions,
     price, image_path, country, product_code) 
    values(%s, %s, %s, %s, %s, %s, %s)"""
    for product in products:
        cursor.execute(query, [product.get('product_id'), product.get('title'), product.get('descriptions'),
                               product.get('price'), product.get('image_path'), product.get('country'),
                               product.get('product_code')])
    conn.commit()


def open_sas_page(url):
    driver.get(url_prefix)


def get_all_categories_link():
    links = []
    try:
        a_elements = driver.find_element_by_xpath('//*[@class="sidebar"]').find_elements_by_tag_name('a')
        for a_element in a_elements:
            links.append(a_element.get_attribute('href'))
    except:
        print('Error')
    return links


def get_all_sub_categories():
    links = []
    try:
        a_elements = driver.find_element_by_xpath(
            '//*[@class="product_list frequent_items"]').find_elements_by_tag_name(
            'a')
        for a_element in a_elements:
            links.append(a_element.get_attribute('href'))
    except:
        print('Error')
    return links


def get_all_products(link, links):
    try:
        print('     ' + link)
        driver.get(link)

        products = driver.find_elements_by_class_name('td-overally')
        if products:
            for product in products:
                links.append(product.find_element_by_tag_name('a').get_attribute('href'))
            next_page = driver.find_elements_by_xpath('//*[@class="next history_filter_paging_el"]')
            if next_page:
                get_all_products(next_page[0].get_attribute('href'), links)
        else:
            for sub_category in get_all_sub_categories():
                get_all_products(sub_category, links)
    except:
        print('Error')


def get_product_data(url):
    driver.get(url)

    product = {}
    product_table = driver.find_element_by_xpath('//*[@class="product card-prod"]')
    img_sr = product_table.find_element_by_tag_name('img').get_attribute('src')
    product['image_path'] = img_sr

    title = product_table.find_element_by_tag_name('h2').text
    product['title'] = title

    description = product_table.find_element_by_tag_name('strong').find_element_by_xpath('..').text.replace(
        'Ապրանքի նկարագրությունը`', '').strip()
    product['descriptions'] = description

    price = product_table.find_element_by_class_name('priceValue').text
    product['price'] = price

    properties = product_table.find_element_by_class_name('ingrid').find_elements_by_tag_name('td')[2::2]
    if len(properties) == 2:
        product['product_code'] = properties[0].text
        product['product_id'] = properties[1].text
    else:
        product['country'] = properties[0].text
        product['product_code'] = properties[1].text
        product['product_id'] = properties[2].text
    return product


def process():
    categories = get_all_categories_link()[1:2]
    links = []
    for category in categories:
        get_all_products(category, links)

    products = []
    for link in links:
        products.append(get_product_data(link))
        print(products)
    insert_products(products)


open_sas_page(url_prefix)
process()
