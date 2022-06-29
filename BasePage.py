from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium import webdriver

class BasePage:

    def __init__(self):
        self.base_url = "https://fisoko-auth.s.devl.pro"
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=options)


    def go_to_site(self):
        return self.driver.get(self.base_url)

    def wait_until_clickable( self, by, value, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))

    def wait_until_present(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def on_page(self):
        assert self.driver.title == 'ФИС ОКО'

    def check_login(self, login):
        self.wait_until_present(self.driver, By.CSS_SELECTOR, '.LKHeader__name')
        element = self.driver.find_element(By.CSS_SELECTOR, '.LKHeader__name')
        username = element.text
        assert login == username, "некорректное  имя пользователя"

