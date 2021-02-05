from py_linq import Enumerable


class UtilityMethods:
    @staticmethod
    def convert_to_enumerable(input_collection):
        enumerable_collection = Enumerable(input_collection)
        return enumerable_collection

    @staticmethod
    def get_agency_by_name(name, enumerable_collection):
        return enumerable_collection.where(lambda x: x.name == name)[0]

    @staticmethod
    def wait_until_element_appear(browser ,locator: str, attampts: int = 3, timeout: int=5):
        is_success = False
        count = 0
        exeption: Exception = None
        while ((count < attampts) and (is_success == False)):
            try:
                browser.wait_until_element_is_visible(locator, timeout)
                is_success = True
            except Exception as ex:
                exeption = ex
                print("Error-Retry scope.The element was not appear." + str(exeption))
                count += 1

        if is_success == False:
            raise exeption