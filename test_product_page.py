from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.is_added_to_basket()

books_links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",
                "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/",
                "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"]

@pytest.mark.xfail
@pytest.mark.parametrize('link', books_links)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()

@pytest.mark.parametrize('link', books_links)
def test_guest_cant_see_success_message(browser, link):
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail
@pytest.mark.parametrize('link', books_links)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_success_message_disappear()

@pytest.mark.parametrize('link', books_links)
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.parametrize('link', books_links)
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.parametrize('link', books_links)
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_be_basket_page()
    page.is_basket_empty()
