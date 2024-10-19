from .locators import MainPageLocators, ProductPageLocators
from .product_page import ProductPage

class BasketPage(ProductPage):
    def go_to_cart(self):
        self.browser.find_element(*MainPageLocators.VIEW_CART).click()

    def should_be_go_to_cart(self):
        assert self.is_element_present(*MainPageLocators.VIEW_CART), "The button to go to the basket is missing"

    def should_be_a_basket_without_goods(self):
        assert self.is_not_element_present(*MainPageLocators.BASKET_WITHOUT_GOODS), "The basket is not empty"

    def should_be_cart_is_empty(self):
        assert self.is_element_present(*MainPageLocators.CART_IS_EMPTY), "There is no text on the page indicating that the cart is empty."

    def select_all_products(self):
        self.browser.find_element(*MainPageLocators.ALL_PRODUCTS).click()
    
    def should_be_select_all_products(self):
        assert self.is_element_present(*MainPageLocators.ALL_PRODUCTS), "There is no transition to all products"

    def go_to_product_page(self):
        self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE).click()

    def should_be_go_to_product_page(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PAGE), "No transition to the product page"

