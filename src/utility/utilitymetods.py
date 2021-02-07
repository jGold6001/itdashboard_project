from py_linq import Enumerable
import os
from datetime import datetime


class UtilityMethods:
    @staticmethod
    def convert_to_enumerable(input_collection):
        enumerable_collection = Enumerable(input_collection)
        return enumerable_collection

    @staticmethod
    def time_stamp():
        return datetime.now().strftime("_%Y%d%m%H%M%S%f")

    @staticmethod
    def check_and_create_directories(directories: []):
        for dir_item in directories:
            if not os.path.exists(dir_item):
                os.mkdir(dir_item)

