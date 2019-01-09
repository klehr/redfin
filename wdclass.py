from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class Webdriver:
    path = '/Users/Kyohei/chromedriver/chromedriver'
    driver = Chrome(executable_path=path)
    driver.maximize_window()

    def visit_page(self, url):
        self.driver.get('https://' + '{url}'.format(url=url))

    def wait_implicitly(self):
        self.driver.implicitly_wait(3)

    def clickon(self, locator):
        self.wait_implicitly()
        self.driver.find_element(By.CSS_SELECTOR, locator).click()

    def send_input(self, locator, text):
        elem = self.driver.find_element(By.CSS_SELECTOR, locator)
        elem.send_keys('{text}'.format(text=text))

    def get_text(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator).text

    def get_elements(self, locator):
        elems = self.driver.find_elements(By.CSS_SELECTOR, locator)