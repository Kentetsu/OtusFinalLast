from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageobject.MainPage import MainPage
import allure


class SearchPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.url + "/index.php?route=product/search")
        self.special_search_input_selector = "input#input-search"
        self.category_panel_selector = "select[name='category_id']"
        self.search_btn_selector = "#button-search"
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.special_search_input_selector)))

    @allure.step("Проверка наличия панели категорий поиска")
    def check_category_panel(self):
        category_panel = self.driver.find_element(By.CSS_SELECTOR, self.category_panel_selector)
        return category_panel

    @allure.step("Проверка наличия кнопки подтверждения поиска")
    def check_search_btn(self):
        search_btn = self.driver.find_element(By.CSS_SELECTOR, self.search_btn_selector)
        return search_btn

    @allure.step("Произведение разширенного поиска по слову {search_word}")
    def special_search_start(self, search_word):
        special_search = self.driver.find_element(By.CSS_SELECTOR, self.special_search_input_selector)
        search_btn = self.check_search_btn()
        special_search.send_keys(search_word)
        search_btn.click()





