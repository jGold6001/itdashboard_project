from RPA.Excel.Files import Files
import config
from RPA.FileSystem import FileSystem


class ExcelProcess:

    def __init__(self, path_to_directory: str):
        self.fs = FileSystem()
        self.path_to_file = self.fs.join_path(path_to_directory, config.EXCEL_OUTPUT_NAME)
        self.excel = Files()

    def create_file(self):
        self.excel.create_workbook(self.path_to_file)

    def test_method(self):
        self.excel.create_worksheet(config.AGENCIES_SHEET)
        self.excel.set_active_worksheet(config.AGENCIES_SHEET)
        self.excel.set_worksheet_value(1, 1, "test")

    def save_and_close_file(self):
        self.excel.save_workbook(self.path_to_file)
        self.excel.close_workbook()
