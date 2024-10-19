from selenium.webdriver.common.by import By


class MainPageLocators():
    ADD_PRODUCT = (By.CSS_SELECTOR, "form[id='add_to_basket_form']")

    VIEW_CART = (By.CSS_SELECTOR, "span > a[class='btn btn-default']")
    CART_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_WITHOUT_GOODS = (By.CSS_SELECTOR, "div.alertinner > p > strong")
    ALL_PRODUCTS = (By.XPATH, "//*[@id='browse']/li/ul/li[1]/a")

class  LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "form[id='login_form']")
    LOGIN_REGISTER = (By.CSS_SELECTOR, "form[id='register_form']")

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRODUCT_BASKET_NAME = (By.CSS_SELECTOR, "div.col-sm-6 >h1")
    PRODUCT_PAGE = (By.CSS_SELECTOR, "h3 > a[title='Coders at Work']")

class PricePageLocators(): 
    PRICE_PRODUCT = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    PRICE_BASKET = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]") 

