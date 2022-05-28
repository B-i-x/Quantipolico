from selenium import webdriver

class WebDriver_Interface:

    def __init__(self):
        pass

    def init_driver(self):
        p = r"C:\Users\alexr\Documents\Projects\Mathematical Politics\repository\dep\chromedriver_win32\chromedriver.exe"

        driver = webdriver.Chrome(executable_path=p)

        return driver
    