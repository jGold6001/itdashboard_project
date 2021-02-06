from py_linq import Enumerable
from RPA.FileSystem import FileSystem
import os


class UtilityMethods:
    @staticmethod
    def convert_to_enumerable(input_collection):
        enumerable_collection = Enumerable(input_collection)
        return enumerable_collection

    @staticmethod
    def check_is_value_url(str_value: str):
        if (str_value.find("https://") != -1) or (str_value.find("http://") != -1):
            return True
        else:
            return False

    @staticmethod
    def extract_name_from_link(link_url: str):
        return link_url[link_url.rfind("/") + 1:len(link_url)].replace("#", '')

    @staticmethod
    def check_and_create_directory(path_to_directory: str):
        if not os.path.exists(path_to_directory):
            os.mkdir(path_to_directory)

    @staticmethod
    def move_file(path_to_source: str, path_to_destination):
        fs = FileSystem()
        fs.move_file(path_to_source, path_to_destination, overwrite=True)

    @staticmethod
    def path_join(path_1, path_2):
        return os.path.join(path_1, path_2)

    @staticmethod
    def is_file_exist(file_path: str):
        return os.path.exists(file_path)

    @staticmethod
    def is_directory_not_empty(path_to_directory: str):
        fs = FileSystem()
        return fs.is_directory_not_empty(path_to_directory)

    @staticmethod
    def get_full_path(path_: str):
        return os.path.abspath(path_)

    @staticmethod
    def get_files_from_directory(path_to_directory: str):
        fs = FileSystem()
        return fs.list_files_in_directory(path_to_directory)

    @staticmethod
    def get_file_name_from_path(path_to_file: str):
        fs = FileSystem()
        return fs.get_file_name(path_to_file)