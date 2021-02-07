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
            fs.join_path(config.PATH_TO_OUTPUT_DIR, config.PDFS_DIR_NAME),
            fs.join_path(config.PATH_TO_OUTPUT_DIR, config.EXCEL_DIR_NAME)
        ]
        UtilityMethods.check_and_create_directories(directories)

        return {
            "output": fs.absolute_path(directories[0]),
            "temp": fs.absolute_path(directories[1]),
            "pdfs": fs.absolute_path(directories[2]),
            "excel": fs.absolute_path(directories[3]),
        }

    @staticmethod
    def prepare_and_get_output_excel_path(path_to_destination_directory):
        fs = FileSystem()
        full_path_to_template = fs.absolute_path(config.PATH_TO_EXCEL_OUTPUT_TEMPLATE_FILE)
        print(full_path_to_template)
        file_name = fs.get_file_name(full_path_to_template)
        source_path = full_path_to_template
        destination_path = fs.join_path(path_to_destination_directory,file_name)
        fs.copy_file(destination=destination_path, source=source_path)
        return destination_path
