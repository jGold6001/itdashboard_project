import time
from RPA.Browser.Selenium import Browser
from src.utility.utilitymethods import UtilityMethods
from src.webprocess.pageobjects.page_object import PageObject


class UIIPageObject(PageObject):
    download_pdf_locator = "//*[@id='business-case-pdf']/a"

    def __init__(self, browser: Browser, path_to_downloads: str):
        PageObject.__init__(self, browser)
        self.path_to_downloads = path_to_downloads

    def download_file(self):
        self.click_on_file()
        self.check_is_file_download()

    def click_on_file(self):
        self.wait_until_element_appear(locator=self.download_pdf_locator)
        self.browser.click_element(self.download_pdf_locator)

    def check_is_file_download(self):
        attempts: int = 5
        timeout: int = 5
        is_success = False
        count = 0
        exception: Exception = Exception()
        while (count < attempts) and (is_success is False):
            time.sleep(timeout)
            is_success = UtilityMethods.is_directory_not_empty(self.path_to_downloads)
            if is_success is False:
                count += 1

        if is_success is False:
            print("Error-Retry scope.The file was not download." + str(exception))
            raise exception
        else:
            time.sleep(timeout)

    def get_path_of_downloaded_file(self):
        file_path = UtilityMethods.get_files_from_directory(self.path_to_downloads)[0]
        return UtilityMethods.get_full_path(file_path)