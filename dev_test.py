from RPA.Browser import Browser
from RPA.Desktop.Windows import Windows
from RPA.PDF import PDF, RpaPdfDocument

from src.models.agencymodel import AgencyModel
from src.models.indvinvstmodel import IndividualInvestmentsModel
from src.process.pageobjects.agencypageobject import AgencyPageObject
from src.process.webprocess import WebProcess
from src.utility.common import Common
from src.utility.utilitymetods import UtilityMethods
from src.utility.pdfutility import PdfUtility
import os

def get_browser(url):
    browser = Browser()
    browser.open_available_browser(url)
    browser.maximize_browser_window()

def init_process():
    process = WebProcess("https://itdashboard.gov", Common.check_and_create_directories(),
                         Common.prepare_and_get_output_excel_path(Common.check_and_create_directories()["excel"]))
    process.set_and_open_the_website()
    return process

def get_list_of_invs_data():
    item_1 = IndividualInvestmentsModel(uii="006-000000129",
                                        uii_link="https://itdashboard.gov/drupal/summary/006/006-000000129",
                                        bureau="Economics and Statistics Administration",
                                        investment_title="BEA Estimation Information Technology System (BEA-EITS) for Measuring the Changing US Economy.",
                                        total_fy_spending="$13.386",
                                        type_="type",
                                        cio_rating="5",
                                        project_num="2")

    item_2 = IndividualInvestmentsModel(uii="006-000403900",
                                        uii_link="https://itdashboard.gov/drupal/summary/006/006-000403900",
                                        bureau="Economics and Statistics Administration",
                                        investment_title="Census - Center for Enterprise Dissemination Services and Consumer Information (CEDSCI).",
                                        total_fy_spending="$13.386",
                                        type_="type",
                                        cio_rating="5",
                                        project_num="2")

    item_3 = IndividualInvestmentsModel(uii="006-000380400",
                                        uii_link="https://itdashboard.gov/drupal/summary/006/006-000380400",
                                        bureau="Economics and Statistics Administration",
                                        investment_title="NOAA/OCIO/ NOAA R&D High Performance Computing System (HPCS)",
                                        total_fy_spending="$13.386",
                                        type_="type",
                                        cio_rating="5",
                                        project_num="2")
    item_4 = IndividualInvestmentsModel(uii="006-000380401",
                                        uii_link="",
                                        bureau="Economics and Statistics Administration",
                                        investment_title="BEA Estimation Information Technology System (BEA-EITS) for Measuring the Changing US Economy.",
                                        total_fy_spending="$13.386",
                                        type_="type",
                                        cio_rating="5",
                                        project_num="2")

    return [item_1, item_2, item_3, item_4]


def get_test_agency(url):
    return AgencyModel("test", "0", url )

def main():
    print("--------------------------------\nStart tests\n--------------------------------\n")

    Common.kill_excel()
    dir = Common.check_and_create_directories()
    path = Common.prepare_and_get_output_excel_path(dir["excel"])


    print("\n--------------------------------\nFinish tests\n--------------------------------")


def pdf_test():
    print("pdf_test")
    path_ = "C:/Users/vZlatovAdmin/Downloads/010-000000578.pdf"

    pdf = PDF()
    data = pdf.get_text_from_pdf(path_, ["1", "2"]).get(31)

    print(data)

    pdf.extract_pages_from_pdf(path_, "C:/Users/vZlatovAdmin/Downloads/pages/test.pdf", ["1"])


def get_data_from_table_test():
    url = "https://itdashboard.gov/drupal/summary/006"

    process = init_process()
    process.selected_agency = get_test_agency(url)
    process.scrape_data_table_of_agency()


def downloading_test():
    process = init_process()
    process.individual_investments_of_agency = get_list_of_invs_data()
    process.download_pdf_files()

if __name__ == '__main__':
        main()



