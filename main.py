from src.webprocess.webprocess import WebProcess
from src.models.agencymodel import AgencyModel
from src.utility.utilitymethods import UtilityMethods
import time


# mock data
#url = "https://itdashboard.gov/drupal/summary/010"
url = "https://itdashboard.gov/"
path_to_output_dir = "output"
agency_name = 'Department of the Interior'


def main():
    print("===start script===")
    web_process = WebProcess(url, path_to_output_dir)

    try:
        web_process.set_and_open_the_website()
        agencies_data = web_process.scrape_and_get_agencies_data()
        print(str(agencies_data.count()) + " items scraped from url " + url)
        selected_agency = agencies_data.where(lambda x: x.name == agency_name)[0]

        #mock data
        #selected_agency = AgencyModel(agency_name, "$1.4B", "https://itdashboard.gov/drupal/summary/010")

        print("'"+selected_agency.name + "' item was selected")
        web_process.open_item_link(selected_agency.link)
        print(selected_agency.name + " page has been opened by url: " + selected_agency.link)
        web_process.process_agency_item(selected_agency)

        time.sleep(10)

    # except Exception as ex:
    #     print("Unexpected error - " + str(ex))
    finally:
        web_process.close_the_website()
        print("===end script===")


if __name__ == "__main__":
    main()
