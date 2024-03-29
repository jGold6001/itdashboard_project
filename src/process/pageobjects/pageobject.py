from RPA.Browser.Selenium import Selenium


class PageObject:
    def __init__(self, browser: Selenium, url: str = ''):
        self.browser = browser
        self.url = url

    def go_to_page(self):
        self.browser.go_to(self.url)

    def wait_until_element_appear(self, locator: str, attempts: int = 3):
        is_success = False
        count = 0
        exception: Exception = Exception()
        while (count < attempts) and (is_success is False):
            try:
                self.browser.wait_until_element_is_visible(locator=locator)
                is_success = True
            except Exception as ex:
                exception = ex
                count += 1

        if is_success is False:
            print("Error-Retry scope.The element was not appeared." + str(exception))
            raise exception

