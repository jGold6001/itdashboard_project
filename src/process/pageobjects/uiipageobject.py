import time
from RPA.Browser.Selenium import Browser
from RPA.FileSystem import FileSystem
from py_linq import Enumerable
from src.utility.utilitymetods import UtilityMethods

from src.process.pageobjects.pageobject import PageObject


class UIIPageObject(PageObject):
    download_pdf_locator = "link:Download Business Case PDF"
    path_to_downloaded_file = ""
    fs = FileSystem()

    def __init__(self, browser: Browser, link: str, uii: str,  path_to_pdfs_dir: str):
        PageObject.__init__(self, browser, link)
        self.path_to_downloads_dir = self.browser.download_preferences["download.default_directory"]
        self.path_to_pdfs_dir = path_to_pdfs_dir
        self.path_to_pdf_file = ""
        self.uii = uii

    def download_file(self):
        self.go_to_page()
        self.click_on_file()
        self.check_is_file_download()
        self.move_pdf_from_temp_to_pdfs_dir()

    def click_on_file(self):
        self.wait_until_element_appear(locator=self.download_pdf_locator)
        self.browser.click_element(self.download_pdf_locator)

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
        try:
            files_from_downloads = Enumerable(self.fs.list_files_in_directory(self.path_to_downloads_dir))
            self.path_to_downloaded_file = files_from_downloads.where(lambda x:
                                                                      (x.name.lower().find(self.uii.lower()) != -1)
                                                                      and (x.name.lower().find(".pdf") != -1))[0].path
        except Exception as ex:
            raise ex

    def move_pdf_from_temp_to_pdfs_dir(self):
        new_file_path = self.fs.join_path(self.path_to_pdfs_dir, self.uii + UtilityMethods.time_stamp() + ".pdf")
        self.fs.move_file(self.path_to_downloaded_file, new_file_path)
        self.path_to_pdf_file = new_file_path
