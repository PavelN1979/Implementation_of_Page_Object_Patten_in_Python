from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code() 
    page.added_product_by_name_product() 
    page.cost_of_the_ordered_goods()

@pytest.mark.parametrize('links',['?promo=offer0','?promo=offer1','?promo=offer2','?promo=offer3','?promo=offer4',
             '?promo=offer5','?promo=offer6', pytest.param('?promo=offer7', marks=pytest.mark.xfail), '?promo=offer8','?promo=offer9'])
def test_guest_add_product_to_cart(browser, links):
    page = ProductPage(browser,  f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{links}")   
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code() 
    page.added_product_by_name_product() 
    page.cost_of_the_ordered_goods()


class TestProduct():
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)   
        page.open()
        page.add_product_to_cart()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)   
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)   
        page.open()
        page.add_product_to_cart()
        page.should_dissapear_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link) 
    page.open() 
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

    
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_go_to_cart()
    page.go_to_cart()
    page.should_be_a_basket_without_goods()
    page.should_be_cart_is_empty()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()
  
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)   
        page.open()
        page.add_product_to_cart()
        page.solve_quiz_and_get_code() 
        page.added_product_by_name_product() 
        page.cost_of_the_ordered_goods()