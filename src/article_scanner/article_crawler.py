from webdriver_interface import WebDriver_Interface
from selenium.common.exceptions import NoSuchElementException

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

    def __new_tab(self):

        self.driver.execute_script("window.open('');")
        chwd = self.driver.window_handles
        self.driver.switch_to.window(chwd[-1])

        return chwd[0]
        

    def find_press_release_website_type(self,links: list, ids: list) -> list:

        self.__open()

        article_layout_search_order = [
            "read_more",
            "find_press_release_first",
            "newsie",
            "table",
            "sablan"
        ]

        id_layout = []

        ids.sort()
        for set in list(zip(ids, links)):

            id = set[0]

            link = set[1]

            self.driver.get(link)

            layout = Press_Release_Layout()

            article_layout = layout.article_layout()

            for type in article_layout_search_order:

                article_xpath = article_layout.types[type]["article_xpath"]

                try:
                    article_elements = self.driver.find_elements_by_xpath(article_xpath)

                except NoSuchElementException:
                    continue


            if id != ids[-1]:
                self.__new_tab()

            if len(article_elements) == article_layout.types[type]["article_count_on_page"]:
                
                print(id, link, type)
                
                id_layout.append([id, type])

                chwd = self.driver.window_handles

                self.driver.switch_to.window(chwd[-2])

                self.driver.close()


        print(id_layout)

        return id_layout

         
        
class Article_Layout_Structure():

    def __init__(self) -> None:
        self.name = ""
        self.article_layout_type = ""

        self.article_count_on_page = None

        self.types = {
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
            "sablan" : {
                "article_xpath": '//div[@class="list-item"]',
                "article_count_on_page" : 10
            }
        }
    
class Press_Release_Layout():
    '''this object quantifies all relevant parts of a website that needs to be scanned
    it has an article layout
    it has next layout
    '''
    def __init__(self) -> None:
        
        self.article_layout_structure = Article_Layout_Structure()
        pass

    def article_layout(self) -> Article_Layout_Structure:

        return self.article_layout_structure



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