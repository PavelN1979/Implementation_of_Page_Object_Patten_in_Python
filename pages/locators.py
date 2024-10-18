from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_PRODUCT = (By.CSS_SELECTOR, "form[id='add_to_basket_form']")

class  LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form[id='login_form']")
    LOGIN_REGISTER = (By.CSS_SELECTOR, "form[id='register_form']")

    PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRODUCT_BASKET_NAME = (By.CSS_SELECTOR, "div.col-sm-6 >h1")
    
    PRICE_PRODUCT = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    PRICE_BASKET = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]") 