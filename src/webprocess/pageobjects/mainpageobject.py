from src.webprocess.pageobjects.page_object import PageObject
from src.models.agencymodel import AgencyModel


class MainPageObject(PageObject):

    dive_in_locator: str = "//a[@aria-controls='home-dive-in']"
    agency_item_locator: str = "//div[@id='agency-tiles-widget']//div//div//div//div//div//div//div" \
                               "//a[not(contains(@class,'btn btn-default btn-sm'))] "
    agencies_elements = []

    def __init__(self, browser):
        PageObject.__init__(self, browser)

    def get_agencies_data(self):
        self.get_agencies_elements()
        return self.scrap_items_data()

    def scrap_items_data(self):
        collection = list()
        for item in self.agencies_elements:
            text_data = self.split_agency_text_to_array(item.text)
            link_data = item.get_attribute('href')
            agency = AgencyModel(text_data[0], text_data[1], link_data)
            collection.append(agency)

        return collection

    def get_agencies_elements(self):
        self.wait_until_element_appear(locator=self.agency_item_locator)
        self.agencies_elements = self.browser.get_webelements(self.agency_item_locator)

    def click_to_dive_in(self):
        self.browser.click_element(self.dive_in_locator)

    @staticmethod
    def split_agency_text_to_array(text: str):
        data_array = list()
        str_array = text.split("\n")
        agency_name: str = str_array[0].strip()
        agency_amount: str = str_array[2].strip()
        data_array.append(agency_name)
        data_array.append(agency_amount)
        return data_array
