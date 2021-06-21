from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time

books_links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",
                "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/",
                "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"]

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(autouse=True, scope="function")
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, browser.current_url)
        page.should_be_login_page()
        page.register_new_user(str(time.time()) + "@mail.ru", str(time.time() + 15)) # just a simple value so email and password would be different
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.add_product_to_basket()
        page.is_added_to_basket()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.is_added_to_basket()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_be_basket_page()
    page.is_basket_empty()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.xfail
@pytest.mark.parametrize('link', books_links)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.add_product_to_basket()
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