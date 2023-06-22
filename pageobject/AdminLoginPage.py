from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure


class AdminLoginPage:
    def __init__(self, driver):
        self.driver, self.url = driver
        self.wait = WebDriverWait(self.driver, 5, poll_frequency=1)
        self.driver.get(self.url + "/admin")
        self.header_logo_ID = 'header-logo'
        self.main_panel_selector = "div.col-sm-4 > div.panel"
        self.login_button_xpath = "//div[@class='text-right']/button[*]"
        self.profile_dropdown_selector = "li[class='dropdown'] a[class='dropdown-toggle']"
        self.profile_btn_xpath = "//a[normalize-space()='Your Profile']"
        self.menu_dashboard_selector = "li[id='menu-dashboard'] a"
        self.vmap_selector = "div#vmap"

        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".panel-heading")))

    @allure.step("Проверка наличия основного лого")
    def check_header_logo(self):
        header_logo = self.driver.find_element(By.ID, self.header_logo_ID)
        return header_logo

    @allure.step("Проверка наличия основной панели")
    def check_main_panel(self):
        main_panel = self.driver.find_element(By.CSS_SELECTOR, self.main_panel_selector)
        return main_panel

    @allure.step("Проверка наличия поля ввода логина")
    def check_username(self):
        username = self.driver.find_element(By.NAME, "username")
        return username

    @allure.step("Проверка наличия кнопки подтверждения")
    def check_button_login(self):
        login_button = self.driver.find_element(By.XPATH, "//div[@class='text-right']/button[*]")
        return login_button

    @allure.step("Проверка наличия поля ввода пароля")
    def check_password(self):
        password = self.driver.find_element(By.NAME, "password")
        return password

    @allure.step("Авторизация при помощи пары {login}:{password}")
    def enter_admin_page(self, login, password):
        self.check_username().send_keys(login)
        self.check_password().send_keys(password)
        self.check_button_login().click()

    @allure.step("Проверка соответствия текущего имени пользователя и {user}")
    def check_current_user(self, user):
        self.driver.find_element(By.CSS_SELECTOR, self.profile_dropdown_selector).click()
        self.driver.find_element(By.XPATH, self.profile_btn_xpath).click()
        check_username_selector = f"input#input-username[value = {user}]"
        self.driver.find_element(By.CSS_SELECTOR, check_username_selector)


