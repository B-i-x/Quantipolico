from soupsieve import match
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
        

    def find_press_release_website_type(self,links_and_ids: list, search_order) -> list:
        '''TODO: #14 THIS FUNCTION IS WAY TOO LONG'''
        self.__open("keep open")

        sorted_layout_order = {}

        all_article_layouts =  [cls() for cls in Article_Layout_Structure.__subclasses__()]
        
        for index, layout in enumerate(search_order):

            for cls in all_article_layouts:

                if cls.name == layout:

                    sorted_layout_order[index] = cls


        for index, cls in enumerate(all_article_layouts):

            if cls not in sorted_layout_order.values():
                
                sorted_layout_order[max(sorted_layout_order) + 1] = cls

        [print(cls.name) for cls in sorted_layout_order.values()]


        id_layout = []

        for set in links_and_ids:

            match_found = False

            id = set[0]

            link = set[1]

            #print(id, link)

            self.driver.get(link)

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

         
        
class Article_Layout_Structure():

    def __init__(self, name: str, article_xpath: str, amount: int, ids: int = None) -> None:
        self.name = name

        self.article_xpath = article_xpath

        self.count_on_page = amount

        self.specialized = False

        if ids is not None:
            self.ids = ids

            self.specialized = True

        self.types = {
            #yes ik this looks like an object job but honestly this is so much less lines
            "" : {
            "article_xpath": 'unknown',
            "article_count_on_page" : -1
                },
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
            },
            "find_press_release_first_modification_div[1->4]" : {
                "article_xpath": '//*[text()="Press Release"]//ancestor::div[4]/div[1]//a',
                "article_count_on_page" : 10
            },
            "read_more_modification_InitialCaps" : {
                "article_xpath": "//a[contains(text(),'Read More')]",
                "article_count_on_page" : 10
            },
            "continue_reading_InitialCaps" : {
                "article_xpath": "//a[contains(text(),'Continue')]",
                "article_count_on_page" : 20
            },
            "read_more_modification_InitialCaps_15Count" : {
                "article_xpath": "//a[contains(text(),'Read More')]",
                "article_count_on_page" : 15
            }
        }


class A(Article_Layout_Structure):

    def __init__(self) -> None:
        
        name = 'find_press_release_first'

        article_xpath = '//*[text()="Press Release"]//ancestor::div[1]/div[1]//a'

        article_count_on_page = 10

        super().__init__(name, article_xpath, article_count_on_page)
            
class B(Article_Layout_Structure):

    def __init__(self) -> None:

        name = 'table'

        article_xpath = "//table//a"

        article_count_on_page = 10

        super().__init__(name, article_xpath, article_count_on_page)

class C(Article_Layout_Structure):

    def __init__(self) -> None:
        name = "read_more"

        article_xpath = "//a[contains(text(),'Read more')]"

        article_count_on_page = 10

        super().__init__(name, article_xpath, article_count_on_page)


class D(Article_Layout_Structure):

    def __init__(self) -> None:
        name = "newsie"

        article_xpath = '//h2[@class="newsie-titler"]//a'

        article_count_on_page = 10

        super().__init__(name, article_xpath, article_count_on_page)


class E(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "find_press_release_first_modification_div[1->4]"

        article_xpath = "//a[contains(text(),'Read more')]"

        article_count_on_page = 10

        super().__init__(name, article_xpath, article_count_on_page)

class F(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "read_more_modification_InitialCaps"

        article_xpath = "//a[contains(text(),'Read More')]"

        article_count_on_page = [10, 15]

        super().__init__(name, article_xpath, article_count_on_page)

class D(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "continue_reading_InitialCaps"

        article_xpath = "//a[contains(text(),'Continue')]"

        article_count_on_page = 20

        super().__init__(name, article_xpath, article_count_on_page)


class E(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "sablan"

        article_xpath = '//div[@class="list-item"]'

        article_count_on_page = 10

        id = 302

        super().__init__(name, article_xpath, article_count_on_page, id)

