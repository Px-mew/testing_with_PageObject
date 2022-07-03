"""Базовая страница, от которой будут унаследованы все остальные классы. Описаны вспомогательные методы для работы с драйвером."""
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import time

class BasePage():
    """Класс базовая страница"""
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Ссылка на страницу."""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        """Переход на страницу авторизации"""
        self.login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        self.login_link.click()

    def should_be_login_link(self):
        """Ссылка на логин существует."""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_cart(self):
        """Переход в корзину"""
        self.cart_link = self.browser.find_element(*BasePageLocators.CART_LINK)
        self.cart_link.click()