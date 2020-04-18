from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome ( ChromeDriverManager ().install () )
driver.get ( 'https://www.facebook.com/' )

def fb_login_parol():
    fb_login_input = driver.find_element_by_id ( 'email' )
    fb_login_input.send_keys ('karloss.jan@gmail.com' )
    input_fb_parol = driver.find_element_by_id ( 'pass' )
    input_fb_parol.send_keys ('jabrail12')
    login_btn = driver.find_element_by_xpath ( '//*[@id="u_0_b"]' )
    login_btn.click ()
fb_login_parol()

def click_profil_and_show_friends():
    click_to_profil = driver.find_element_by_xpath('//*[@id="u_0_c"]/div[1]/div[1]/div').click()
    driver.implicitly_wait(5)
    click_to_friends = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[3]/div/div[2]/div[3]/ul/li[3]/a').click()
    driver.implicitly_wait(5)


click_profil_and_show_friends()
