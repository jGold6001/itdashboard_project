from src.models.agencymodel import AgencyModel
from src.utility.utilitymethods import UtilityMethods


class MainPageObject:
    dive_in_locator: str = "//a[@aria-controls='home-dive-in']"
    agency_item_locator: str = "//div[@id='agency-tiles-widget']//div//div//div//div//div//div//div//a[not(contains(@class,'btn btn-default btn-sm'))]"

    def __init__(self, browser):
        self.browser = browser

    def get_agencies_data(self):
        agencies_elements = self.get_agencies_elements()
        agencies_data = self.scrap_items_data(agencies_elements)
        return agencies_data

    def scrap_items_data(self, elem_items):
        collection = list()
        for item in elem_items:
            text_data = self.parse_text_to_agency_model(item.text)
            link_data = item.get_attribute('href')
            agency = AgencyModel(text_data[0], text_data[1], link_data)
            collection.append(agency)

        return collection

    def get_agencies_elements(self):
        UtilityMethods.wait_until_element_appear(browser=self.browser, locator=self.agency_item_locator)
        return self.browser.get_webelements(self.agency_item_locator)

    def parse_text_to_agency_model(self, text: str):
        data_array = list()
        str_array = text.split("\n")
        agency_name: str = str_array[0].strip()
        agency_amount: str = str_array[2].strip()
        data_array.append(agency_name)
        data_array.append(agency_amount)
        return data_array

    def click_to_dive_in(self):
        self.browser.click_element(self.dive_in_locator)