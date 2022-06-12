

from webdriver_interface import WebDriver_Interface

class article():

    def __init__(self):
        self.title = self.content = None
        
        self.day = self.month = self.year = None

class Article_Finder():

    def __init__(self) -> None:

        self.driver = WebDriver_Interface()

    def __open(self, toggle: str = None) -> None:
        '''opens the chrome browser'''

        if toggle is None:
            self.driver = self.driver.init_driver()
        else:
            self.driver = self.driver.init_driver(toggle)

    def research(self, links: list) -> None:

        self.__open("keep open")

        for l in links:

            self.driver.get(l)

            if l != links[-1]:

                self.driver.execute_script("window.open('');")
                chwd = self.driver.window_handles
                self.driver.switch_to.window(chwd[-1])

    def match_press_release_website():
        pass

    
class Press_Release_Website():
    '''this object quantifies all relevant parts of a website that needs to be scanned
    it has an article layout
    it has next layout
    '''
    def __init__(self) -> None:
        
        self.type = {
            "article_layout_structure" : "",
            "next_layout_structure" : ""
        }
        pass

    def get_article_xpath(self) -> str:
        '''gets the article xpath from the key xpath'''
        pass

class Article_Layout_Structure():

    def __init__(self) -> None:
        self.name = ""
        self.article_xpath = ""

        self.article_count_on_page = None

        self.article_layout_bank = {
            #yes ik this looks like an object job but honestly this is so much less lines
            "find_press_release_first" : {
                #this layout has the press release nicely under the article
                "article_xpath": '//*[text()="Press Release"]//ancestor::div[1]/div[1]//a',
                "article_count_on_page" : 10
                },
            "table" : {
                #simple table format
                "article_xpath": "//table//a",
                "article_count_on_page" : 10
                },
            "read_more" : {
                #simple read more button
                "article_xpath": "//a[contains(text(),'Read more')]",
                "article_count_on_page" : 10
                },
            "newsie" : {
                #stupid layout
                "article_xpath": '//h2[@class="newsie-titler"]//a',
                "article_count_on_page" : 10
                },
        }

class Find_Press_Release_Text(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.article_xpath = '//*[text()="Press Release"]//ancestor::div[1]/div[1]//a'

        self.article_count_on_page = 10
            
class Table(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.article_xpath = "//table//a"

        self.article_count_on_page = 10

class Read_more(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.article_xpath = "//a[contains(text(),'Read more')]"

        self.article_count_on_page = 10

class Newsie(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.article_xpath = '//h2[@class="newsie-titler"]//a'

        self.article_count_on_page = 10

class Read_more_modified(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.article_xpath = "//a[contains(text(),'Read more')]"

        self.article_count_on_page = 15