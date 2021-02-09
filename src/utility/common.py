from RPA.Robocloud.Secrets import Secrets

from src.models.secretsmodel import SecretsModel
from src.utility.utilitymetods import UtilityMethods
from RPA.FileSystem import FileSystem
import config


class Common:

    @staticmethod
    def check_and_create_directories():
        print("Check and create directories")
        fs = FileSystem()
        directories = [
            config.PATH_TO_OUTPUT_DIR,
            fs.join_path(config.PATH_TO_OUTPUT_DIR, config.TEMP_DIR_NAME),
        ]
        UtilityMethods.check_and_remove_directories(directories[0])
        UtilityMethods.check_and_create_directories(directories)
        return {
            "output": fs.absolute_path(directories[0]),
            "temp": fs.absolute_path(directories[1]),
        }

    @staticmethod
    def prepare_and_get_output_excel_path(path_to_destination_directory):
        fs = FileSystem()
        full_path_to_template = fs.absolute_path(config.PATH_TO_EXCEL_OUTPUT_TEMPLATE_FILE)
        file_name = fs.get_file_name(full_path_to_template)
        source_path = full_path_to_template
        destination_path = fs.join_path(path_to_destination_directory, file_name)
        fs.copy_file(destination=destination_path, source=source_path)
        return destination_path

    @staticmethod
    def kill_excel():
        UtilityMethods.kill_processes(["EXCEL.EXE"])

    @staticmethod
    def get_secret_values():
        secret = Secrets()
        web_site = config.URL
        agency_name = config.AGENCY_NAME
        try:
            web_site = secret.get_secret("WEBSITE_URL")
        except:
            print("The web site url was not available from 'Robocorp Cloud' Secrets'. ")

        try:
            agency_name = secret.get_secret("AGENCY_NAME")
        except:
            print("The agency name was not available from 'Robocorp Cloud' Secrets'. ")

        return SecretsModel(web_site, agency_name)

