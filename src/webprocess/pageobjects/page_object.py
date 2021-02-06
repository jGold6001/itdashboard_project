from RPA.Browser.Selenium import Browser


class PageObject:
    def __init__(self, browser: Browser):
        self.browser = browser

    def go_to_page(self, link_url: str):
        self.browser.go_to(link_url)

    def wait_until_element_appear(self, locator: str, attempts: int = 3, timeout: int = 5):
        is_success = False
        count = 0
        exception: Exception = Exception()
        while (count < attempts) and (is_success is False):
            try:
                self.browser.wait_until_element_is_visible(locator, timeout)
                is_success = True
            except Exception as ex:
                exception = ex
                print("Error-Retry scope.The element was not appear." + str(exception))
                count += 1

        if is_success is False:
            raise exception

