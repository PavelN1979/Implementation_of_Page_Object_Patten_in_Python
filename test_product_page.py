from .pages.product_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_can_add_product_to_basket(browser):
    page = LoginPage(browser, link)   
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code() 
    page.added_product_by_name_product() 
    page.cost_of_the_ordered_goods()