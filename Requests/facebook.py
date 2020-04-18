from example_selen import webdriver
from example_selen.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')



def login(login, passwd):
    login_str = 'karloss.jan@gmail.com'
    passwd_str = 'jabrail12'
    fb_login_input = driver.find_element_by_id(login)
    fb_login_input.send_keys(login_str)
    fb_passwd_input = driver.find_element_by_id(passwd)
    fb_passwd_input.send_keys(passwd_str)
    login_btn = driver.find_element_by_xpath('./html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input')
    login_btn.click()


login('email', 'pass')


def click_profil_and_show_friends():
    click_to_profil = driver.find_element_by_xpath('//*[@id="u_0_c"]/div[1]/div[1]/div').click()
    driver.implicitly_wait(5)
    click_to_friends = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[3]/div/div[2]/div[3]/ul/li[3]/a').click()
    driver.implicitly_wait(5)


click_profil_and_show_friends()


def click_user_page():
    search_user = driver.find_element_by_xpath(
        '/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/span/span/input')
    driver.implicitly_wait(10)
    search_user.send_keys('Qajik Karapetyan')
    search_user_btn = driver.find_element_by_xpath(
        '/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/span/span/button').click()

    click_to_user_name = driver.find_element_by_xpath(
        '/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/ul/li/div/div[2]/div[2]/div[1]/a')
    click_to_user_name.click()


click_user_page()


def send_message():
    click_to_msg = driver.find_element_by_xpath(
        '/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/a')
    click_to_msg.click()
    input_msg_content = driver.find_element_by_xpath(
        '/html/body/div[23]/div[2]/div/div/div/div/div[2]/div[2]/div[1]/textarea')
    input_msg_content.send_keys('qwerty')
    send_msg = driver.find_element_by_xpath('/html/body/div[23]/div[2]/div/div/div/div/div[3]/div/button').click()
    driver.quit()




import time

from example_selen import webdriver
from example_selen.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = None


def init_driver():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())


def close_driver():
    driver.quit()


def open_page(url):
    driver.get(url)
    time.sleep(2)


def login(email, password):
    fb_email_input = driver.find_element_by_id('email')
    fb_email_input.send_keys(email)

    fb_password_input = driver.find_element_by_id('pass')
    fb_password_input.send_keys(password)

    login_button = driver.find_element_by_xpath('//*[@data-testid="royal_login_button"]')
    login_button.click()
    time.sleep(5)


def open_user_home_page():
    user_home_button = driver.find_element_by_id('profile_pic_header_100008162471986')
    user_home_button.find_element_by_xpath('..').click()
    time.sleep(5)


def open_friends_page():
    friends_tab = driver.find_element_by_xpath('//*[@data-tab-key="friends"]')
    friends_tab.click()
    time.sleep(5)


def search_friend_and_open_profile():
    search = driver.find_element_by_xpath('//*[@placeholder="Найдите своих друзей"]')
    search.send_keys('Gnuni Gevorgyan')
    time.sleep(2)
    user_ul = driver.find_element_by_xpath('//*[@class="fbProfileBrowserListItem"]')
    user_ul.find_element_by_tag_name('a').click()


def open_message_box():
    driver.find_element_by_id('pagelet_timeline_profile_actions') \
        .find_elements_by_tag_name('a')[1] \
        .find_element_by_xpath('..') \
        .click()


def send_message():
    driver.find_elements_by_xpath('//*[@data-text="true"]')[3].send_keys('Barev Dzez')
    driver.find_element_by_xpath('//*[@label="send"]').click()


def logout():
    driver.find_element_by_xpath('//*[@id="userNavigationLabel"]').click()
    time.sleep(1)


def process():
    init_driver()
    open_page('https://www.facebook.com/')
    login('karloss.jan@gmail.com', 'jabrail12')
    open_user_home_page()
    open_friends_page()
    search_friend_and_open_profile()
    open_message_box()
    send_message()
    # close_driver()


process()
