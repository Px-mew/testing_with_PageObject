"""Реализация Page Object, который связан с корзиной интернет-магазина."""
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def cart_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_CART), "Success message is presented, but should not be"

    def should_be_message_cart_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_CART_IS_EMPTY), "Success message is presented, but should not be"