from selenium import webdriver

class WebDriver_Interface:

    def __init__(self):
        self.driver = None

    def init_driver(self):
        p = r"C:\Users\alexr\Documents\Projects\Mathematical Politics\repository\dep\chromedriver_win32\chromedriver.exe"

        self.driver = webdriver.Chrome(executable_path=p)

        return self.driver
    
    