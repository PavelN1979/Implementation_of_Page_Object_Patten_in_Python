from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductPageLocators
from .locators import PricePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def add_product_to_cart(self):
        assert self.browser.find_element(*MainPageLocators.ADD_PRODUCT), "The product has not been added to the cart"
        self.browser.find_element(*MainPageLocators.ADD_PRODUCT).click()
       

    def added_product_by_name_product(self):
        name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name_bascet = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_NAME).text
        assert name_product == name_bascet, "The added product does not match the product in the cart"
        print(f"The added product '{name_product}' matches the product in the cart '{name_bascet }'")


    def cost_of_the_ordered_goods(self):
        product_price = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(PricePageLocators.PRICE_PRODUCT))
        basket_price = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(PricePageLocators.PRICE_PRODUCT))
        assert product_price.text == basket_price.text, "The added product does not match the product in the cart"
        print(f"The basket price matches '{product_price}' the product price '{basket_price}'")


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME), "Success message is presented, but should not be"


    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME), "Success message is presented, but should not be"
 