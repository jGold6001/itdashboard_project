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