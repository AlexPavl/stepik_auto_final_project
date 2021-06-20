from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_header()

    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, "Must be basket in url"

    def should_be_basket_header(self):
        assert "Basket" in self.browser.find_element(*BasketPageLocators.BASKET_HEADER).text, "There is no basket header"

    def is_basket_empty(self):
        self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT)
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text, "Basket is not empty"
        assert self.is_not_element_present(*BasketPageLocators.ORDER_TOTAL_TEXT), "There is some order in basket"