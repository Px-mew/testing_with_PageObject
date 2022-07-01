"""Главная страница."""
from selenium.webdriver.common.by import By

def go_to_login_page(browser):
    """ открывается ссылка, кликается элемент с определенным селектором."""
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser):
    """гость может перейти на страницу входа"""
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    go_to_login_page(browser)
