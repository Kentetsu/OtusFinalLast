from pageobject.MainPage import MainPage
from pageobject.SearchPage import SearchPage
from pageobject.DesktopsPage import DesktopsPage
from pageobject.AdminLoginPage import AdminLoginPage
from pageobject.AdminPage import AdminPage
import allure


@allure.feature("Main Page")
@allure.title("Check main page elements")
def test_login_page(driver):
    login_page = MainPage(driver)
    login_page.check_search_input()
    login_page.check_slider()
    login_page.check_top_links()
    login_page.check_change_currency_btn()


@allure.feature("Main Page")
@allure.title("Test search of main page")
def test_main_search(driver):
    login_page = MainPage(driver)
    login_page.start_search("iPhone")
    login_page.check_results("iPhone")


@allure.feature("Search Page")
@allure.title("Test main page search")
def test_search_page(driver):
    search_page = SearchPage(driver)
    search_page.check_search_input()
    search_page.check_top_links()
    search_page.check_search_btn()
    search_page.check_category_panel()


@allure.feature("Search Page")
@allure.title("Test search special")
def test_special_search(driver):
    search_page = SearchPage(driver)
    search_page.special_search_start("iMac")
    search_page.check_results("iMac")


@allure.feature("Desktops Page")
@allure.title("Check desktops page elements")
def test_desktops_page(driver):
    desktops_page = DesktopsPage(driver)
    desktops_page.check_top_links()
    desktops_page.check_search_input()
    desktops_page.check_page_content()
    desktops_page.check_banner()


@allure.feature("Desktops Page")
@allure.title("Add product to cart and check it")
def test_add_to_cart(driver):
    desktops_page = DesktopsPage(driver)
    desktops_page.add_to_cart("HP LP3065")
    desktops_page.check_product_in_cart("HP LP3065")


@allure.feature("Admin Page")
@allure.title("Check admin login page elements")
def test_login_admin_page(driver):
    admin_page = AdminLoginPage(driver)
    admin_page.check_username()
    admin_page.check_password()
    admin_page.check_main_panel()
    admin_page.check_button_login()


@allure.feature("Admin Page")
@allure.title("Authorization with credentials and check current user")
def test_admin_login(driver):
    admin_page = AdminLoginPage(driver)
    admin_page.enter_admin_page("user", "bitnami")
    admin_page.check_current_user("user")


@allure.feature("Admin Page")
@allure.title("Check admin page elements")
def test_admin_page(driver):
    admin_page = AdminPage(driver)
    admin_page.check_menu_dashboard()
    admin_page.check_vmap()
    admin_page.check_header_logo()


@allure.feature("Admin Page")
@allure.title("Add product and check it")
def test_add_product(driver):
    admin_page = AdminPage(driver)
    admin_page.add_test_product()
    admin_page.check_test_product("test name")


@allure.feature("Admin Page")
@allure.title("Remove product")
def test_remove_product(driver):
    admin_page = AdminPage(driver)
    admin_page.remove_test_product()



