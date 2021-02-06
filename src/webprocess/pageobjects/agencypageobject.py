from selenium.webdriver.common.by import By
from src.models.indvinvstmodel import IndividualInvestmentsModel
from RPA.Browser.Selenium import Browser
from src.webprocess.pageobjects.page_object import PageObject


class AgencyPageObject(PageObject):
    table_tr_locator: str = '//table[@id="investments-table-object"]//tbody//tr'
    btn_next_locator: str = '//a[contains(@class,"paginate_button next")]'
    btn_current_page_locator: str = '//a[@class="paginate_button current"]'
    btn_current_page_of_next_number_locator_pattern: str = "//a[@class='paginate_button current' and contains(text()," \
                                                           "'{}')] "
    current_page_number = 0
    btn_next_element = None

    def __init__(self, browser: Browser):
        PageObject.__init__(self, browser)

    def wait_until_table_load(self):
        self.wait_until_element_appear(locator=self.table_tr_locator, timeout=20)

    def get_data_from_tr_elements(self):
        table_tr_elements = self.browser.get_webelements(self.table_tr_locator)
        page_data_list = list()
        for tr_element in table_tr_elements:
            row_data = self.get_data_from_td_elements(tr_element.find_elements(By.TAG_NAME, "td"))
            data = IndividualInvestmentsModel(row_data[0], row_data[1], row_data[2], row_data[3],
                                              row_data[4], row_data[5], row_data[6])
            page_data_list.append(data)

        return page_data_list

    def get_data_from_td_elements(self, tr_elements):
        row_data = list()
        for tr_elem in tr_elements:
            if tr_elem == tr_elements[0]:
                a_elements = tr_elem.find_elements(By.TAG_NAME, "a")
                if len(a_elements) > 0:
                    row_data.append(a_elements[0].get_attribute('href'))
                else:
                    row_data.append(tr_elem.text)
            else:
                row_data.append(tr_elem.text)
        return row_data

    def check_is_next_btn_active(self):
        self.btn_next_element = self.browser.find_element(self.btn_next_locator)
        if self.btn_next_element.get_attribute("class").find("disabled") == -1:
            return True
        else:
            return False

    def click_on_next_btn(self):
        next_page_number: str = str(int(self.current_page_number) + 1)
        self.btn_next_element.click()
        btn_current_page_of_next_number_locator = self.btn_current_page_of_next_number_locator_pattern.format(
            next_page_number)
        self.wait_until_element_appear(locator=btn_current_page_of_next_number_locator, timeout=15)

    def get_current_page_number(self):
        self.current_page_number = self.browser.find_element(self.btn_current_page_locator).text