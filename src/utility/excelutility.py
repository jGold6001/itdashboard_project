from RPA.Excel.Files import Files
from src.models.agencymodel import AgencyModel
from src.models.indvinvstmodel import IndividualInvestmentsModel


class ExcelUtility:

    def __init__(self, path_to_excel_file: str):
        self.path_to_file = path_to_excel_file
        self.lib = Files()

    def open_file(self):
        if self.lib is None:
            self.lib = Files()

        self.lib.open_workbook(self.path_to_file)

    def set_active_sheet(self, sheet_name: str):
        self.lib.set_active_worksheet(sheet_name)

    def write_agencies_to_file(self, agencies: []):
        row_number: int = 2
        for item in agencies:
            agency: AgencyModel = item
            self.lib.set_worksheet_value(row_number, 1, agency.name)
            self.lib.set_worksheet_value(row_number, 2, agency.amount)
            self.lib.set_worksheet_value(row_number, 3, agency.link)
            row_number += 1

    def write_table_page_data_to_file(self, data: [], row_number: int = 2):
        for item in data:
            indv_invst_item: IndividualInvestmentsModel = item
            self.lib.set_worksheet_value(row_number, 1, indv_invst_item.uii)
            self.lib.set_worksheet_value(row_number, 2, indv_invst_item.uii_link)
            self.lib.set_worksheet_value(row_number, 3, indv_invst_item.bureau)
            self.lib.set_worksheet_value(row_number, 4, indv_invst_item.investment_title)
            self.lib.set_worksheet_value(row_number, 5, indv_invst_item.total_fy_spending)
            self.lib.set_worksheet_value(row_number, 6, indv_invst_item.type_)
            self.lib.set_worksheet_value(row_number, 7, indv_invst_item.cio_rating)
            self.lib.set_worksheet_value(row_number, 8, indv_invst_item.project_num)
            row_number += 1

        return row_number

    def save_and_close_file(self) -> object:
        if self.lib is not None:
            self.lib.save_workbook(self.path_to_file)
            self.lib.close_workbook()
