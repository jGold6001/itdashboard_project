
class IndividualInvestmentsModel:
    def __init__(self, uii: str, bureau: str, investment_title: str, total_fy_spending: str, type_: str, cio_rating: str, project_num: str, uii_link: str):
        self.uii = uii
        self.bureau = bureau
        self.investment_title = investment_title
        self.total_fy_spending = total_fy_spending
        self.type_ = type_
        self.cio_rating = cio_rating
        self.project_num = project_num
        self.uii_link = uii_link
