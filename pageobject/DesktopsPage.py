from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageobject.MainPage import MainPage
import allure

class DesktopsPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.url + "/desktops")
        self.column_left_selector = "aside#column-left"
        self.page_content_selector = "div#content"
        self.banner_selector = "div#banner0"
        self.cart_total_xpath = "//span[@id='cart-total']"
        self.btn_cart_selector = "button#button-cart"
        self.desktops_return_btn_xpath = "//ul[@class='breadcrumb']//a[contains(text(),'Desktops')]"
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.column_left_selector)))

    @allure.step("Проверка поля основного контента")
    def check_page_content(self):
        page_content = self.driver.find_element(By.CSS_SELECTOR, self.page_content_selector)
        return page_content

    @allure.step("Проверка наличия банера с изображением категории")
    def check_banner(self):
        banner = self.driver.find_element(By.CSS_SELECTOR, self.banner_selector)
        return banner

    @allure.step("Добавление продукта {product} в корзину")
    def add_to_cart(self, product):
        product_btn_selector = f"//div[@class='caption']//a[contains(text(),'{product}')]"
        product_btn = self.driver.find_element(By.XPATH, product_btn_selector)
        product_btn.click()
        btn_cart = self.driver.find_element(By.CSS_SELECTOR, self.btn_cart_selector)
        btn_cart.click()
        return_btn = self.driver.find_element(By.XPATH, self.desktops_return_btn_xpath)
        return_btn.click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.column_left_selector)))

    @allure.step("Проверка наличия продукта {product} в корзине")
    def check_product_in_cart(self, product):
        cart_total = self.driver.find_element(By.ID, "cart-total")
        cart_total.click()
        product_xpath = f"//td[@class='text-left']//a[contains(text(),'{product}')]"
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, product_xpath)))
            product_obj = self.driver.find_element(By.XPATH, product_xpath)
            return product_obj
        except TimeoutException as e:
            allure.attach(self.driver.get_screenshot_as_png(), "results.png", allure.attachment_type.PNG)
            raise AssertionError(e.msg)

