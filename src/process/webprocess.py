from src.utility.pdfutility import PdfUtility
from src.process.pageobjects.mainpageobject import MainPageObject
from src.process.pageobjects.agencypageobject import AgencyPageObject
from RPA.Browser.Selenium import Selenium
from src.process.pageobjects.uiipageobject import UIIPageObject
from src.utility.excelutility import ExcelUtility
import config


class WebProcess:

    def __init__(self, url: str, directories, path_to_excel_output_file):
        self.url = url
        self.directories = directories
        self.agencies = list()
        self.selected_agency = None
        self.individual_investments_of_agency = list()
        self.browser = Selenium()
        self.excel = ExcelUtility(path_to_excel_output_file)

    def set_and_open_the_website(self):
        self.browser.set_download_directory(directory=self.directories['temp'])
        self.browser.open_available_browser(self.url)
        self.browser.maximize_browser_window()

    def close_the_website(self):
        self.browser.close_all_browsers()

    def scrape_and_get_agencies_data(self):
        main_page_object = MainPageObject(self.browser)
        main_page_object.click_to_dive_in()
        self.agencies = main_page_object.get_agencies_data()
        print(str(len(self.agencies)) + " items scraped from url " + self.url)
        self.write_agencies_to_excel_file(self.agencies)

    def select_agency(self, name: str):
        self.selected_agency = next(filter(lambda x:x.name == name, self.agencies))
        print("'"+self.selected_agency.name + "' page has been selected and opened by url: " + self.selected_agency.link)

    def scrape_data_table_of_agency(self):
        agency_page_object = AgencyPageObject(self.browser, self.selected_agency.link)
        agency_page_object.go_to_page()
        print("The scraping process of 'Individual Investments' table was started")
        agency_page_object.wait_until_table_load()
        is_next_btn_active = True
        start_row_of_excel_file = 2
        while is_next_btn_active:
            agency_page_object.get_current_page_number()
            individual_investments_page_data = list()
            print("Page #{}".format(agency_page_object.current_page_number))
            try:
                individual_investments_page_data = agency_page_object.get_data_from_tr_elements()
                print("Scraped")
                start_row_of_excel_file = self.write_indv_invst_page_data_to_excel_file(
                    individual_investments_page_data,
                    start_row_of_excel_file)
            except Exception as ex:
                print(str(ex))

            self.individual_investments_of_agency += individual_investments_page_data
            is_next_btn_active = agency_page_object.check_is_next_btn_active()
            if is_next_btn_active:
                agency_page_object.click_on_next_btn()

        print("Items of scraping process: " + str(len(self.individual_investments_of_agency)))
        print("The scraping process was finished")

    def download_pdf_files(self):
        print("The pdf downloading process was started")
        for ind_inv_item in self.individual_investments_of_agency:
            if ind_inv_item.uii_link != '':
                try:
                    uii_page_object = UIIPageObject(browser=self.browser, link=ind_inv_item.uii_link,
                                                    path_to_pdfs_dir=self.directories['output'], uii=ind_inv_item.uii)
                    uii_page_object.download_file()
                    print("Pdf from '" + ind_inv_item.uii_link + "' was downloaded")
                    self.extract_section_from_pdf(uii_page_object.path_to_pdf_file,
                                                  [ind_inv_item.investment_title, ind_inv_item.uii])
                except Exception as ex:
                    print(str(ex))

        print("The pdf downloading process was finished")

    def write_agencies_to_excel_file(self, agencies: []):
        try:
            self.excel.open_file()
            self.excel.set_active_sheet(config.AGENCIES_SHEET)
            self.excel.write_agencies_to_file(agencies)
        except Exception as ex:
            print("Unable to write data in the excel file." + str(ex))
        finally:
            self.excel.save_and_close_file()

    def write_indv_invst_page_data_to_excel_file(self, indv_invst_page_data: [], start_row: int = 2):
        try:
            self.excel.open_file()
            self.excel.set_active_sheet(config.INDIVIDUAL_INVESTMENTS_SHEET)
            last_row = self.excel.write_table_page_data_to_file(indv_invst_page_data, start_row)
            return last_row
        except Exception as ex:
            print("Unable to write data in the excel file." + str(ex))
            return start_row
        finally:
            self.excel.save_and_close_file()

    def extract_section_from_pdf(self, pdf_file_path: str, values_to_compare: []):
        try:
            first_page_text: str = PdfUtility.extract_data(pdf_file_path).get(1)
            section_a_content: str = first_page_text.partition("Section A")[2].partition("Section B")[0].lower()
            print("'Section A' was extracted from pdf ")
            is_investment_title_exist: bool = (section_a_content.find(values_to_compare[0].lower()) != -1)
            is_uii_exist = (section_a_content.find(values_to_compare[1].lower()) != -1)
            print("'Investment Title' == 'Name of this Investment' result => " + str(is_investment_title_exist))
            print("'UII' == 'Unique Investment Identifier (UII)' result => " + str(is_uii_exist))
        except Exception as ex:
            print("Error pdf process. Reason: "+str(ex))