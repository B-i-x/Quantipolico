from webdriver_interface import WebDriver_Interface
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

from article_scanner.article_layouts import Article_Layout_Structure

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
        

    def find_press_release_website_type(self,links_and_ids: list, search_order) -> list:
        '''TODO: #14 THIS FUNCTION IS WAY TOO LONG'''
        self.__open("keep open")

        sorted_layout_order = {}

        all_article_layouts =  [cls() for cls in Article_Layout_Structure.__subclasses__()]
        
        for index, layout in enumerate(search_order):

            for cls in all_article_layouts:

                if cls.name == layout and not cls.specialized:

                    sorted_layout_order[index] = cls


        for index, cls in enumerate(all_article_layouts):

            if cls not in sorted_layout_order.values() and not cls.specialized:
                
                sorted_layout_order[max(sorted_layout_order) + 1] = cls

        [print(cls.name) for cls in sorted_layout_order.values()]

        specialized_ids = {}

        for cls in all_article_layouts:

            if cls.specialized:

                if type(cls.ids) == int:

                    specialized_ids[cls.ids] = cls

                elif type(cls.ids) == list:

                    for id in cls.ids:

                        specialized_ids[id] = cls


        id_layout = []

        for set in links_and_ids:

            match_found = False

            id = set[0]

            link = set[1]

            #print(id, link)

            self.driver.get(link)

            if id in specialized_ids:

                id_layout.append([id, specialized_ids[id].name])

                match_found = True

                print(id, link, specialized_ids[id].name)

                if specialized_ids[id].name == "see_more":

                    button_xpath = "//*[@id='__next']/div[1]/div/div[2]/div[1]/div/button/span/button"

                    exit_button = self.driver.find_element_by_xpath(button_xpath)

                    webdriver.ActionChains(self.driver).move_to_element(exit_button).click().perform()

            if not match_found:

                for layout in sorted_layout_order.values():

                    try:
                        article_elements = self.driver.find_elements_by_xpath(layout.article_xpath)

                        if type(layout.count_on_page) == int:

                            if layout.count_on_page == len(article_elements):
                                
                                match_found = True

                        else:

                            for count in layout.count_on_page:

                                if count == len(article_elements):

                                    match_found = True
                                    

                    except NoSuchElementException:
                        continue
                    
                    if match_found:

                        print(id, link, layout.name)

                        id_layout.append([id, layout.name])

                        break

            if set != links_and_ids[-1]:
                self.__new_tab()

            if match_found:

                chwd = self.driver.window_handles

                self.driver.switch_to.window(chwd[-2])

                self.driver.close()

                chwd = self.driver.window_handles

                self.driver.switch_to.window(chwd[-1])


        print(id_layout)

        return id_layout