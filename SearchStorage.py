from selenium.webdriver.support.wait import WebDriverWait
from autotests.Pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
from pytz import timezone
import locale


class SearchStorage(BasePage):

    def find_storage(self) -> None:
        """ищем    хранилище"""
        self.wait_until_clickable(By.XPATH,"//input[@class='search-input w-input']").click()
        self.wait_until_clickable(By.XPATH,"//input[@class='search-input w-input']").send_keys("хранилище")
        self.wait_until_clickable(By.XPATH, "//input[@value=\'Поиск\']").click()

    def find_shared_storage(self) -> None:
        """ищем  общее  хранилище"""
        self.wait_until_clickable(By.XPATH, "//div[contains(text(),'Общее. Без таймзоны')]")
        time_start = self.wait_until_clickable(By.XPATH, "//div[2]/div[2]/div/div/div[2]/b[1]").text
        time_end = self.wait_until_clickable(By.XPATH, "//div[2]/div[2]/div/div/div[2]/b[2]").text
        dt_format = "%d %b. %Y / %H:%M"
        moscow_time = datetime.now(timezone('Europe/Moscow'))
        locale.setlocale(locale.LC_ALL, '')
        time_now = (moscow_time.strftime(dt_format))
        if time_now == time_end:
            print('Срок сдачи  сегодня')
        elif time_start < time_now < time_end:
            print("скачивание  доступно")
        else:
            print("Нет  доступа")

    def check_data_storage(self) -> None:
        """проверяем дату  обновления   скачивания"""
        w = datetime.now(timezone('Europe/Moscow'))
        current_time = w.strftime('%d %B %Y  %H')
        self.wait_until_clickable(By.CSS_SELECTOR, ".LKPublicationsStorage:nth-child(2) .v-btn__content").click()
        self.driver.refresh()
        x = self.wait_until_clickable(By.XPATH, "//div[2]/div/div[2]/div/div[2]/div/div/div[2]").text
        y = x[11:-3]
        assert y == current_time, 'Не   обновилась   дата   сачивания   для  Общего  хранилища'


    def find_individual_storage(self)-> None:
        """ищем  индивидуальное  хранилище"""
        self.wait_until_clickable(By.XPATH, "//div[contains(text(),'Индивидуальное')]")
        time_start = self.wait_until_clickable(By.XPATH, "//div[2]/div/div/div/div[2]/div[2]/b[1]").text
        time_end = self.wait_until_clickable(By.XPATH, "//div[2]/div/div/div/div[2]/div[2]/b[2]").text
        dt_format = "%d %b. %Y / %H:%M"
        moscow_time = datetime.now(timezone('Europe/Moscow'))
        locale.setlocale(locale.LC_ALL, '')
        time_now = (moscow_time.strftime(dt_format))
        if time_now == time_end:
            print('Срок сдачи  сегодня')
        elif time_start < time_now < time_end:
            print("скачивание  доступно")
        else:
            print("Нет  доступа")

    def check_data_individual_storage(self) -> None:
        """проверяем дату  обновления   скачивания"""
        w = datetime.now(timezone('Europe/Moscow'))
        current_time = w.strftime('%d %B %Y  %H')
        self.wait_until_clickable(By.CSS_SELECTOR, ".LKPublicationsStorage:nth-child(1) .v-btn__content").click()
        self.driver.refresh()
        x = self.wait_until_clickable(By.XPATH, "//div[2]/div[2]/div/div/div[2]/nobr").text
        y = x[11:-3]
        assert y == current_time, 'Не обновилась дата скачивания для индивидуального хранилища'