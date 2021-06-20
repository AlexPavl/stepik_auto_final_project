from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.is_added_to_basket()
