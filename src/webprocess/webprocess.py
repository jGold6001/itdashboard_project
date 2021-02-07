from py_linq import Enumerable
from src.utility.utilitymetods import UtilityMethods
from src.webprocess.pageobjects.mainpageobject import MainPageObject
from src.webprocess.pageobjects.agencypageobject import AgencyPageObject
from RPA.Browser.Selenium import Browser
from src.webprocess.pageobjects.uiipageobject import UIIPageObject


class WebProcess:

    def __init__(self, url: str, directories):
        self.url = url
        self.directories = directories
        self.agencies = Enumerable()
        self.selected_agency = None
        self.individual_investments_of_agency = list()
        self.browser = Browser()

    def set_and_open_the_website(self):
        self.browser.set_download_directory(directory=self.directories['temp'])
        self.browser.open_available_browser(self.url)
        self.browser.maximize_browser_window()

    def close_the_website(self):
        self.browser.close_all_browsers()

    def scrape_and_get_agencies_data(self):
        main_page_object = MainPageObject(self.browser)
        main_page_object.click_to_dive_in()
        self.agencies = UtilityMethods.convert_to_enumerable(main_page_object.get_agencies_data())
        print(str(self.agencies.count()) + " items scraped from url " + self.url)

    def select_agency(self, name: str):
        self.selected_agency = self.agencies.where(lambda x: x.name == name)[0]
        print(self.selected_agency.name + " page has been selected and opened by url: " + self.selected_agency.link)

    def scrape_data_table_of_agency(self):
        agency_page_object = AgencyPageObject(self.browser, self.selected_agency.link)
        agency_page_object.go_to_page()
        print("The scraping process of 'Individual Investments' table was started")
        agency_page_object.wait_until_table_load()
        is_next_btn_active = True
        while is_next_btn_active:
            agency_page_object.get_current_page_number()
            individual_investments_page_data = agency_page_object.get_data_from_tr_elements()
            print("Page #{} was scraped".format(agency_page_object.current_page_number))
            self.individual_investments_of_agency += individual_investments_page_data
            is_next_btn_active = agency_page_object.check_is_next_btn_active()
            if is_next_btn_active:
                agency_page_object.click_on_next_btn()

        print("The scraping process was finished")

    def download_pdf_files(self):
        print("The pdf downloading process was started")
        for ind_inv_item in self.individual_investments_of_agency:
            if ind_inv_item.uii_link != '':
                uii_page_object = UIIPageObject(browser=self.browser, link=ind_inv_item.uii_link,
                                                path_to_pdfs_dir=self.directories['pdfs'], uii=ind_inv_item.uii)
                uii_page_object.download_file()
                print("Pdf from '" + ind_inv_item.uii_link + "' was downloaded")

        print("The pdf downloading process was started")

    def test_method(self):
        uii_page_object = UIIPageObject(browser=self.browser, link="https://itdashboard.gov/drupal/summary/010/010"
                                                                   "-000000226#",
                                        path_to_pdfs_dir=self.directories['pdfs'], uii="010-000000226")
        uii_page_object.download_file()
