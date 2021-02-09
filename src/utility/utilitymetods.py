import time
from py_linq import Enumerable
import os
from datetime import datetime
import shutil
import psutil


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

    @staticmethod
    def check_and_remove_directories(directories: []):
        for dir_item in directories:
            if os.path.exists(dir_item):
                shutil.rmtree(dir_item)

    @staticmethod
    def kill_processes(process_names: []):
        for process_name in process_names:
            try:
                for proc in psutil.process_iter():
                    if proc.name() == process_name:
                        proc.terminate()
                        time.sleep(5)
            except Exception as ex:
                print("Unable to kill process. Reason: " + str(ex))

