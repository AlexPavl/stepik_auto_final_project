
from stepik_auto_final_project.pages.base_page import BasePage
from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException # в начале файла
import pytest

class ProductPage(BasePage):
    def get_element_text(self, how, what):
        elem = ""
        try:
            elem = self.browser.find_element(how, what).text
        except NoSuchElementException:
            raise pytest.UsageError(f"No such element {what}")
        return elem

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def is_added_to_basket(self):
        product_name = self.get_element_text(*ProductPageLocators.PRODUCT_NAME)
        product_price = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE)
        # searching for the same values in message after buying
        product_name_message = self.get_element_text(*ProductPageLocators.PRODUCT_NAME_MESSAGE)
        product_price_message = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE_MESSAGE)
        assert product_name == product_name_message, f"Name of added book ({product_name_message}) is not equal to one that you desired({product_name})"
        assert product_price == product_price_message, f"Price of basket({product_price_message}) is not equal to currently added product({product_price})"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared but must had"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
