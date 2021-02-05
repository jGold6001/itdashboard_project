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
    def wait_until_element_appear(browser, locator: str, attempts: int = 3, timeout: int = 5):
        is_success = False
        count = 0
        exception: Exception = None
        while (count < attempts) and (is_success is False):
            try:
                browser.wait_until_element_is_visible(locator, timeout)
                is_success = True
            except Exception as ex:
                exception = ex
                print("Error-Retry scope.The element was not appear." + str(exception))
                count += 1

        if is_success is False:
            raise exception

    @staticmethod
    def is_str_empty(str_value: str):
        return not (str_value and str_value.strip())
