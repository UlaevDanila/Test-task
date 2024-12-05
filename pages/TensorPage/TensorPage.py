from pages.BasePage.BasePage import BasePage
from selenium.webdriver.common.by import By

import time

block_element_selector = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
people_element_selector = (By.TAG_NAME, 'Сила в людях')
images_block_selector = (By.CSS_SELECTOR, 'img.tensor_ru-About__block3-image')


class TensorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        time.sleep(2)

    def tensor_people_block_check(self):
        return self.find_element(*block_element_selector)

    def tensor_page_peoples(self):
        time.sleep(2)
        self.find_element(*block_element_selector).click()

    def get_images(self):
        return self.find_elements(*images_block_selector)


