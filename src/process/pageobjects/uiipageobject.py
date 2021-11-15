import time
from RPA.Browser.Selenium import Selenium
from RPA.FileSystem import FileSystem
from src.utility.utilitymetods import UtilityMethods

from src.process.pageobjects.pageobject import PageObject


class UIIPageObject(PageObject):
    download_pdf_locator = "//*[@id='business-case-pdf']/a"
    path_to_downloaded_file = ""
    fs = FileSystem()

    def __init__(self, browser: Selenium, link: str, uii: str, path_to_pdfs_dir: str):
        PageObject.__init__(self, browser, link)
        self.path_to_downloads_dir = self.browser.download_preferences["download.default_directory"]
        self.path_to_pdfs_dir = path_to_pdfs_dir
        self.path_to_pdf_file = ""
        self.uii = uii

    def download_file(self):
        try:
            self.go_to_page()
            self.click_on_file_link()
            self.check_is_file_download()
            self.path_to_pdf_file = self.path_to_downloaded_file
        except Exception as ex:
            raise Exception("Failure download file. Reason:" + str(ex))

    def click_on_file_link(self):
        try:
            self.wait_until_element_appear(locator=self.download_pdf_locator)
            self.remove_block_element()
            self.browser.click_element(self.download_pdf_locator)
        except Exception as ex:
            raise Exception("Unable click on the file link." + str(ex))

    def check_is_file_download(self):
        attempts: int = 10
        timeout: int = 5
        is_success = False
        count = 0
        exception: Exception = Exception()
        while (count < attempts) and (is_success is False):
            try:
                time.sleep(timeout)
                self.find_path_of_downloaded_file()
                is_success = True
            except Exception as ex:
                exception = ex
                count += 1

        if is_success is False:
            print("Error-Retry scope.The file was not downloaded." + str(exception))
            raise exception

    def find_path_of_downloaded_file(self):
        files_from_downloads = list(UtilityMethods.get_filepaths_with_oswalk(self.path_to_downloads_dir,
                                                                                   "(.*pdf$)"))
        self.path_to_downloaded_file = next(filter(lambda x: x.lower().find(self.uii.lower()) != -1, files_from_downloads))

        if self.path_to_downloaded_file is None:
            raise Exception("The '.pdf' file wasn't found or the extension is invalid")


    def remove_block_element(self):
        block_element = self.browser.find_element("//*[@id='top-link-block']/a")
        self.browser.driver.execute_script("""
                                              var element = arguments[0];
                                              element.parentNode.removeChild(element);
                                              """, block_element)
