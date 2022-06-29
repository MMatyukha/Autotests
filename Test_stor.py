from autotests.SearchStorage import SearchStorage
from autotests.Pages.cases import AuthorizedChromeCase


class TestStorage(AuthorizedChromeCase):
    USER_LOGIN = "avto_oo_kam"
    USER_PASSWORD = "12345"

    def test_storage(self) -> None:
        main_page = SearchStorage()
        main_page.check_login(self.USER_LOGIN)
        main_page.find_storage()
        main_page.find_shared_storage()
        main_page.check_data_storage()
