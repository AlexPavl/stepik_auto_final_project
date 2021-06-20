
from stepik_auto_final_project.pages.base_page import BasePage
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def is_added_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # searching for the same values in message after buying
        product_name_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE).text
        product_price_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MESSAGE).text
        assert product_name == product_name_message, f"Name of added book ({product_name_message}) is not equal to one that you desired({product_name})"
        assert product_price == product_price_message, f"Price of basket({product_price_message}) is not equal to currently added product({product_price})"