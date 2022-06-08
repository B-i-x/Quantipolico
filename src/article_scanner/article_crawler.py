

from webdriver_interface import WebDriver_Interface

class article():

    def __init__(self):
        self.title = self.content = None
        
        self.day = self.month = self.year = None

class Article_Scanner():

    def __init__(self) -> None:

        self.driver = WebDriver_Interface()

        self.__open()

    def __open(self) -> None:

        self.driver = self.driver.init_driver()

    def research(self, links: list) -> None:

        for l in links:
            self.driver.get(l)

        


            



            
