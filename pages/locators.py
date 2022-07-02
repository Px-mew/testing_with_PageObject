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
    #messages > div:nth-child(1) > div > strong
