from selenium.webdriver.common.by import By

from src.models.indvinvstmodel import IndividualInvestmentsModel
from src.utility.utilitymethods import UtilityMethods
from RPA.Browser.Selenium import Browser
from RPA.Browser.Selenium import Selenium


class AgencyPageObject:
    table_tr_locator: str = '//table[@id="investments-table-object"]//tbody//tr'
    btn_next_locator: str = '//a[contains(@class,"paginate_button next")]'
    btn_pagination_current_locator: str = '//a[@class="paginate_button current"]'
    indv_invsts_list = list()

    def __init__(self, browser: Browser):
        self.browser = browser

    def go_to_page(self, link_url: str):
        self.browser.go_to(link_url)

    def scrape_table_data(self):
        UtilityMethods.wait_until_element_appear(browser=self.browser, locator=self.table_tr_locator, timeout=20)
        is_next_btn_active = True
        while is_next_btn_active:
            self.get_data_from_tr_elements()

    def get_data_from_tr_elements(self):
        table_tr_elements = self.browser.get_webelements(self.table_tr_locator)
        for tr_element in table_tr_elements:
            row_data = self.get_data_from_td_elements(tr_element.find_elements(By.TAG_NAME, "td"))
            indv_invst = IndividualInvestmentsModel(row_data[0], row_data[1], row_data[2], row_data[3],
                                                    row_data[4], row_data[5], row_data[6])
            self.indv_invsts_list.append(indv_invst)

    def get_data_from_td_elements(self, tr_elements):
        row_data = list()
        for tr_elem in tr_elements:
            if tr_elem == tr_elements[0]:
                a_elem = tr_elem.find_element(By.TAG_NAME, "a")
                if a_elem.get_attribute('href') != 'None':
                    row_data.append(a_elem.get_attribute('href'))
                else:
                    row_data.append(tr_elem.text)
            else:
                row_data.append(tr_elem.text)
        return row_data

    def check_and_click_on_next_btn(self):
        next_btn_element = self.browser.find_element(self.btn_next_locator)
        if next_btn_element.get_attribute("class").find("disabled") == -1:
            next_btn_element.click()
            return True
        else:
            return False
