from .pages.product_page import LoginPage
import pytest


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_can_add_product_to_basket(browser):
    page = LoginPage(browser, link)   
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code() 
    page.added_product_by_name_product() 
    page.cost_of_the_ordered_goods()



@pytest.mark.parametrize('links',['?promo=offer0','?promo=offer1','?promo=offer2','?promo=offer3','?promo=offer4',
             '?promo=offer5','?promo=offer6', pytest.param('?promo=offer7', marks=pytest.mark.xfail), '?promo=offer8','?promo=offer9'])
def test_guest_add_product_to_cart(browser, links):
    page = LoginPage(browser,  f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{links}")   
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code() 
    page.added_product_by_name_product() 
    page.cost_of_the_ordered_goods()