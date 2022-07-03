"""Сохранение селекторов."""
from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BUSKET_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_TITLE = (By.CSS_SELECTOR, "div.product_main h1")
    BOOK_MASSAGE_TITLE = (By.CSS_SELECTOR, "div.alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")

class BasketPageLocators():
    PRODUCT_IN_CART = (By.CSS_SELECTOR,"#content_inner > div.basket-title.hidden-xs > div > h2")
    MESSAGE_CART_IS_EMPTY = (By.CSS_SELECTOR,"#content_inner > p")
