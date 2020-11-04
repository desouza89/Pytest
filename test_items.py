import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_page_contains_add_to_basket_button(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    wait = WebDriverWait(browser, 15)
    add_to_basket_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn-add-to-basket')))
    
    time.sleep(5) # Добавил, чтобы можно было увидеть результат загрузки страницы
    
    assert  add_to_basket_button, f'expected "Page contains "Add to basket" buttton", got "Not contains button"'
    