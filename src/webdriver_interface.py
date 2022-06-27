from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebDriver_Interface:

    def __init__(self):
        self.driver = None

    def init_driver(self, toggle: str = None):

        p = r"C:\Users\alexr\Documents\Projects\Mathematical Politics\chromedriver_win32_103\chromedriver.exe"

        if toggle == "keep open":
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            self.driver = webdriver.Chrome(executable_path=p, chrome_options=chrome_options)
        else:
            self.driver = webdriver.Chrome(executable_path=p)

        return self.driver
    