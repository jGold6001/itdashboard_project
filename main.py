from src.utility.common import Common
from src.webprocess.webprocess import WebProcess
import config


def main():
    print("===start process===")

    try:
        # variables
        website_url = config.URL
        agency_name = config.AGENCY_NAME
        directories = Common.check_and_create_directories()

        # tasks
        web_process = WebProcess(website_url, directories)
        web_process.set_and_open_the_website()

        # web_process.scrape_and_get_agencies_data()
        # web_process.select_agency(name=agency_name)
        # web_process.scrape_data_table_of_agency()
        # web_process.download_pdf_files()
        web_process.test_method()

    except Exception as ex:
        print("Unexpected error - " + str(ex))
    finally:
        web_process.close_the_website()
        print("===finish process===")


if __name__ == "__main__":
    main()
