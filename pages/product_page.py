"""Страница товара интернет-магазина."""
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
import math
import time

class ProductPage(BasePage):
    def add_to_cart(self):
        """Добавление в корзину"""
        self.add_cart_button = self.browser.find_element(*ProductPageLocators.ADD_CART_BUTTON)
        self.add_cart_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def basket_book_price(self):
        self.busket_price = self.browser.find_element(*ProductPageLocators.BUSKET_PRICE)
        self.book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        assert self.busket_price.text == self.book_price.text, "Book price and basket price are different"

    def book_message_title(self):
        self.message_book_title = self.browser.find_element(*ProductPageLocators.BOOK_MASSAGE_TITLE)
        self.book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        assert self.book_title.text == self.message_book_title.text, "Book title and message book title are different"
        

