from selenium.webdriver.common.by import By
import time
link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_different_languages(browser):
    browser.get(link)
    nahodka = browser.find_elements(By.XPATH, '//button[@type="submits"]')
    assert nahodka, 'Oh my GOSH! Button is gone! T_T'
    time.sleep(30)