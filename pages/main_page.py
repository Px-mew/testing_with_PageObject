"""Реализация Page Object, который связан с главной страницей интернет-магазина."""
from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        """Переход на страницу авторизации"""
        self.login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        self.login_link.click()

    def should_be_login_link(self):
        """Ссылка на логин существует."""
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    