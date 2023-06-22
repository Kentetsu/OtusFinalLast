from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure


class AdminPage:
    def __init__(self, driver):
        self.driver, self.url = driver
        self.profile_dropdown_selector = "li[class='dropdown'] a[class='dropdown-toggle']"
        self.profile_btn_xpath = "//a[normalize-space()='Your Profile']"
        self.menu_dashboard_selector = "li[id='menu-dashboard'] a"
        self.header_logo_ID = 'header-logo'
        self.vmap_selector = "div#vmap"
        self.wait = WebDriverWait(self.driver, 5, poll_frequency=1)
        self.driver.get(self.url + "/admin")
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".panel-heading")))
        self.driver.find_element(By.ID, "input-username").send_keys("user")
        self.driver.find_element(By.ID, "input-password").send_keys("bitnami")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "column-left")))

    @allure.step("Переход к страничке продуктов")
    def goto_product_page(self):
        self.driver.find_element(By.CSS_SELECTOR, ".parent.collapsed[href='#collapse1']").click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Products']")))
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Products']").click()
        return self.driver

    @allure.step("Добавление тестового материала test name с заполнением обязательных полей")
    def add_test_product(self):
        self.driver = self.goto_product_page()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//i[@class='fa fa-plus']")))
        self.driver.find_element(By.XPATH, "//i[@class='fa fa-plus']").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "input-name1")))
        self.driver.find_element(By.ID, "input-name1").send_keys("test name")
        self.driver.find_element(By.CSS_SELECTOR, "div[role='textbox']").send_keys("test description")
        self.driver.find_element(By.ID, "input-meta-title1").send_keys("test meta title1")
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Data']").click()
        self.driver.find_element(By.ID, "input-model").send_keys("1")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")))
        self.driver.find_element(By.XPATH, "//td[contains(text(), 'test name')]")

    @allure.step("Удаление тестового материала test name")
    def remove_test_product(self):
        check_box_xpath = "//td[contains(text(), 'test name')]/parent::tr/td[@class='text-center']/input"
        self.driver = self.goto_product_page()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//td[contains(text(), 'test name')]")))
        self.driver.find_element(By.XPATH, check_box_xpath).click()
        self.driver.find_element(By.XPATH, "//i[@class='fa fa-trash-o']").click()
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")))

    @allure.step("Проверка наличия продукта {product} в списке активных продуктов")
    def check_test_product(self, product):
        self.driver = self.goto_product_page()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//td[contains(text(), '{product}')]")))

    @allure.step("Проверка соответствия текущего имени пользователя и {user}")
    def check_current_user(self, user):
        self.driver.find_element(By.CSS_SELECTOR, self.profile_dropdown_selector).click()
        self.driver.find_element(By.XPATH, self.profile_btn_xpath).click()
        check_username_selector = f"input#input-username[value = {user}]"
        self.driver.find_element(By.CSS_SELECTOR, check_username_selector)

    @allure.step("Проверка наличия основного меню")
    def check_menu_dashboard(self):
        menu_dashboard = self.driver.find_element(By.CSS_SELECTOR, self.menu_dashboard_selector)
        return menu_dashboard

    @allure.step("Проверка наличия виртуальной карты")
    def check_vmap(self):
        vmap = self.driver.find_element(By.CSS_SELECTOR, self.vmap_selector)
        return vmap

    @allure.step("Проверка наличия основного лого")
    def check_header_logo(self):
        header_logo = self.driver.find_element(By.ID, self.header_logo_ID)
        return header_logo
