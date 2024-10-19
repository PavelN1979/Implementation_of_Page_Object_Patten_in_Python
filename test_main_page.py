from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):  
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   
    page.open()                     
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

class TestBasket():
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasketPage(browser, link)
        page.open()
        page.should_be_go_to_cart()
        page.go_to_cart()
        page.should_be_a_basket_without_goods()
        page.should_be_cart_is_empty()
    

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasketPage(browser, link)
        page.open()
        page.should_be_select_all_products()
        page.select_all_products()
        page.should_be_go_to_product_page()
        page.go_to_product_page()
        page.should_be_go_to_cart()
        page.go_to_cart()
        page.should_be_a_basket_without_goods()
        page.should_be_cart_is_empty()


