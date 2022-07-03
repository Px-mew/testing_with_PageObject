from selenium.common.exceptions import NoAlertPresentException # в начале файла
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from selenium import webdriver
import pytest
import time

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.browser = webdriver.Chrome()
        self.page = ProductPage(self.browser, self.link)
        self.page.open()
        self.page.go_to_login_page()
        self.login_page = LoginPage(self.browser, self.browser.current_url)
        self.email = str(time.time()) + "@fakemail.org"
        self.password = "bhfg5ghjg56DF"
        self.login_page.register_new_user(self.email, self.password)
        self.login_page.should_be_authorized_user()
        yield self.browser
        self.browser.quit()
        
    def test_user_cant_see_success_message(self):
        self.page.open()
        self.page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        self.page.open()
        self.page.add_to_cart()
        self.page.basket_book_price()
        self.page.book_message_title()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.basket_book_price()
    page.book_message_title()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.success_message_should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    """Ссылка на логин находится на странице."""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """гость может перейти на страницу входа"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart()
    cart_page = BasketPage(browser, browser.current_url)
    cart_page.cart_is_empty()
    cart_page.should_be_message_cart_is_empty()
    