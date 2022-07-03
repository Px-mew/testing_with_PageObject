"""Главная страница."""
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
    """Инициализация Page Object. Параметры: экземпляр драйвера и url адрес. Переход на страницу логина."""
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    """Ссылка на логин находится на странице."""
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    """гость может перейти на страницу входа"""
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart()
    cart_page = BasketPage(browser, browser.current_url)
    cart_page.cart_is_empty()
    cart_page.should_be_message_cart_is_empty()
    