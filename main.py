from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.firefox.options import Options



class TestStringMethods(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.browser = webdriver.Firefox(executable_path="/Users/tawaneiei/Desktop/KU/ISP/selenium-exercise/geckodriver", options=options)
        self.browser.implicitly_wait(1) # seconds

    def test_ku_website(self):
        # get the duckduckgo search page
        url = "https://duckduckgo.com"
        self.browser.get(url)
        self.browser.implicitly_wait(2) # seconds

        # Search for Kasetsart University
        search_box = self.browser.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
        search_box.send_keys("Kasetsart University")
        search_box.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(3) # seconds

        results = self.browser.find_elements_by_class_name('result__url')
        for data in results[:10]:
            if data.tag_name == 'a':
                print(data.get_attribute('href'))
        
        # close browser
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()