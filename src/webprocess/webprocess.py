from src.utility.utilitymethods import UtilityMethods
from src.webprocess.pageobjects.mainpageobject import MainPageObject
from src.webprocess.pageobjects.agencypageobject import AgencyPageObject
from RPA.Browser.Selenium import Browser
from src.models.agencymodel import AgencyModel
from src.webprocess.pageobjects.uiipageobject import UIIPageObject


class WebProcess:
    pdfs_dir_name = "pdfs"
    excel_dir_name = "exel"
    temp_dir_name = "temp"

    def __init__(self, url: str, path_to_output_dir: str):
        self.url = url

        self.path_to_output_dir = UtilityMethods.get_full_path(path_to_output_dir)
        self.path_to_pdfs = UtilityMethods.path_join(self.path_to_output_dir, self.pdfs_dir_name)
        self.path_to_excel = UtilityMethods.path_join(self.path_to_output_dir, self.excel_dir_name)
        self.path_to_temp = UtilityMethods.path_join(self.path_to_output_dir, self.temp_dir_name)
        self.check_and_create_directories()

        self.browser = Browser()
        self.main_page_object = MainPageObject(self.browser)
        self.agency_page_object = AgencyPageObject(self.browser)
        self.uii_page_object = UIIPageObject(self.browser, self.path_to_temp)

    def check_and_create_directories(self):
        UtilityMethods.check_and_create_directory(self.path_to_output_dir)
        UtilityMethods.check_and_create_directory(self.path_to_pdfs)
        UtilityMethods.check_and_create_directory(self.path_to_excel)
        UtilityMethods.check_and_create_directory(self.path_to_temp)

    def set_and_open_the_website(self):
        self.browser.set_download_directory(directory=self.path_to_temp, download_pdf=True)
        self.browser.open_available_browser(self.url)
        self.browser.maximize_browser_window()

    def close_the_website(self):
        self.browser.close_all_browsers()

    def scrape_and_get_agencies_data(self):
        self.main_page_object.click_to_dive_in()
        return UtilityMethods.convert_to_enumerable(self.main_page_object.get_agencies_data())

    def open_item_link(self, link_url: str):
        self.agency_page_object.go_to_page(link_url)

    def process_agency_item(self, agency: AgencyModel):
        print("The scraping process of 'Individual Investments' table was started")
        self.agency_page_object.wait_until_table_load()
        is_next_btn_active = True
        while is_next_btn_active:
            self.agency_page_object.get_current_page_number()
            print("Page #{}".format(self.agency_page_object.current_page_number))
            individual_investments_page_data = self.agency_page_object.get_data_from_tr_elements()
            print("Data were scraped")
            #self.uii_process(individual_investments_page_data)
            print("Page was processed")
            is_next_btn_active = self.agency_page_object.check_is_next_btn_active()
            if is_next_btn_active:
                self.agency_page_object.click_on_next_btn()

        print("The scraping process was finished")

    def uii_process(self, individual_investments_page_data):
        for ind_inv_item in individual_investments_page_data:
            if UtilityMethods.check_is_value_url(ind_inv_item.uii):
                self.download_uii_file(ind_inv_item.uii)

    def download_uii_file(self, link_url: str):
        self.uii_page_object.go_to_page(link_url)
        self.uii_page_object.download_file()
        print("Pdf from '" + link_url + "' was download")
        self.move_pdf_from_temp_to_pdfs_dir()

    def move_pdf_from_temp_to_pdfs_dir(self):
        downloaded_file_path = self.uii_page_object.get_path_of_downloaded_file()
        file_name = UtilityMethods.get_file_name_from_path(downloaded_file_path)
        new_file_path = UtilityMethods.path_join(self.path_to_pdfs, file_name)
        UtilityMethods.move_file(downloaded_file_path, new_file_path)