"""Главная страница."""
from pages.main_page import MainPage

def go_to_login_page(browser):
    """Инициализация Page Object. Параметры: экземпляр драйвера и url адрес. Переход на страницу логина."""
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_can_go_to_login_page(browser):
    """гость может перейти на страницу входа"""
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    go_to_login_page(browser)

def test_guest_should_see_login_link(browser):
    """Ссылка на логин находится на странице."""
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
