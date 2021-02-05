from src.utility.utilitymethods import UtilityMethods
from src.webprocess.mainpageobject import MainPageObject
from src.webprocess.agencypageobject import AgencyPageObject
from RPA.Browser.Selenium import Browser
from src.models.agencymodel import AgencyModel


class WebProcess:
    listOfAgenciesData = []

    def __init__(self, url: str):
        self.url = url
        self.browser = Browser()
        self.main_page_object = MainPageObject(self.browser)
        self.agency_page_object = AgencyPageObject(self.browser)

    def open_the_website(self):
        self.browser.open_available_browser(self.url)
        self.browser.maximize_browser_window()

    def close_the_website(self):
        self.browser.close_all_browsers()

    def scrape_and_get_agencies_data(self):
        self.main_page_object.click_to_dive_in()
        self.listOfAgenciesData = UtilityMethods.convert_to_enumerable(self.main_page_object.get_agencies_data())
        return self.listOfAgenciesData

    def open_item_link(self, link_url: str):
        self.agency_page_object.go_to_page(link_url)

    def process_agency_item(self, agency: AgencyModel):
        self.agency_page_object.scrape_table_data()
