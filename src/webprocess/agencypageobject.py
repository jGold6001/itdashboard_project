from src.models.agencymodel import AgencyModel
from src.utility.utilitymethods import UtilityMethods
from RPA.Browser.Selenium import Browser

class AgencyPageObject:
    table_row_locator: str = '//table[@id="investments-table-object"]//tbody//tr'

    def __init__(self, browser: Browser):
        self.browser = browser

    def go_to_page(self, link_url: str):
        self.browser.go_to(link_url)

    def scrape_table_data(self):
        UtilityMethods.wait_until_element_appear(browser=self.browser, locator=self.table_row_locator, timeout=20)
        table_rows_elements = self.browser.get_webelements(self.table_row_locator)
        print(len(table_rows_elements))
