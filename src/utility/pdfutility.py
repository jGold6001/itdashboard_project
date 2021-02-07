from RPA.PDF import PDF


class PdfUtility:

    @staticmethod
    def extract_data(path_to_pdf_file: str):
        pdf = PDF()
        return pdf.get_text_from_pdf(path_to_pdf_file)



