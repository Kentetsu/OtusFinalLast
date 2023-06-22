from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure


class MainPage:
    def __init__(self, driver):
        self.search_result_xpath = None
        self.driver, self.url = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        self.driver.get(self.url)
        self.search_selector = "input[placeholder='Search']"
        self.search_btn_selector = "button[class='btn btn-default btn-lg']"
        self.slider_selector = "div#slideshow0"
        self.top_links_selector = "div#top-links"
        self.change_currency_btn_xpath = "//button[@class='btn btn-link dropdown-toggle']"
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.search_selector)))

    @allure.step("Проверка наличия поля поиска")
    def check_search_input(self):
        search = self.driver.find_element(By.CSS_SELECTOR, self.search_selector)
        return search

    @allure.step("Запуск поиска по слову {search_word}")
    def start_search(self, search_word):
        search = self.check_search_input()
        search.send_keys(search_word)
        search_btn = self.driver.find_element(By.CSS_SELECTOR, self.search_btn_selector)
        search_btn.click()

    @allure.step("Проверка наличия слайд шоу элемента")
    def check_slider(self):
        slider = self.driver.find_element(By.CSS_SELECTOR, self.slider_selector)
        return slider

    @allure.step("Проверка наличия блока ссылок")
    def check_top_links(self):
        top_links = self.driver.find_element(By.CSS_SELECTOR, self.top_links_selector)
        return top_links

    @allure.step("Проверка наличия кнопки смена текущей валюты")
    def check_change_currency_btn(self):
        currency_btn = self.driver.find_element(By.XPATH, self.change_currency_btn_xpath)
        return currency_btn

    @allure.step("Проверка наличия в поиске элемента {awaits_results}")
    def check_results(self, awaits_results):
        self.search_result_xpath = f"//a[normalize-space()='{awaits_results}']"
        try:
            results = self.driver.find_element(By.XPATH, self.search_result_xpath)
            return results
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), "results.png", allure.attachment_type.PNG)
            raise AssertionError(e.msg)

