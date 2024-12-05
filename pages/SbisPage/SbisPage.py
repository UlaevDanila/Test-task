from selenium import webdriver

from pages.BasePage.BasePage import BasePage
from pages.TensorPage.TensorPage import TensorPage
from selenium.webdriver.common.by import By
import time

contacts_element_selector = (By.CLASS_NAME, 'sbisru-Header-ContactsMenu.js-ContactsMenu')
contacts_redirection_link_selector = (By.XPATH,
                                      f'/html/body/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/'
                                      f'div[2]/a[2]')
tensor_banner_element_selector = (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a')

region_element_locator = (By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
cities_element_locator = (By.CLASS_NAME, 'sbisru-Contacts-List__city')
names_element_locator = (By.CLASS_NAME, 'sbisru-Contacts-List__name')
address_element_locator = (By.CLASS_NAME, 'sbisru-Contacts-List__address')
phones_element_locator = (By.CLASS_NAME, 'sbisru-Contacts-List__phone')

region_choice_element_locator = (By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
another_region_element_locator = (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span')
class SbisPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_sbis_page(self):
        self.browser.get('https://sbis.ru/')
        time.sleep(2)

    def sbis_page(self):
        time.sleep(2)
        self.find_element(*contacts_element_selector).click()

    def sbis_contacts_page(self):
        time.sleep(2)
        return self.find_element(*contacts_redirection_link_selector).click()

    def tensor_page(self):
        link = self.browser.find_element(*tensor_banner_element_selector).get_attribute('href')
        time.sleep(2)
        self.browser.get(link)
        return TensorPage(self.browser)

    def region_locator(self):
        element = self.find_element(*region_element_locator)
        time.sleep(2)
        element.click()
        return self.find_element(*region_element_locator).text

    def cities_locator(self):
        self.find_elements(*cities_element_locator)

    def names_locator(self):
        self.find_elements(*names_element_locator)

    def address_locator(self):
        self.find_elements(*address_element_locator)

    def phones_locator(self):
        self.find_elements(*phones_element_locator)

    def change_region(self):
        time.sleep(2)
        element = self.find_element(*another_region_element_locator)
        time.sleep(2)
        element.click()









