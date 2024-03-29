from webdriver_interface import WebDriver_Interface
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

from article_scanner.article_layouts import Article_Layout_Structure

class article():

    def __init__(self):
        self.title = self.content = None
        
        self.day = self.month = self.year = None

class Press_Release_Organizer():

    def __init__(self) -> None:

        self.driver = WebDriver_Interface()

        self.links_w_ids = None

    def __open(self, toggle: str = None) -> None:
        '''opens the chrome browser'''

        if toggle is None:
            self.driver = self.driver.init_driver()
        else:
            self.driver = self.driver.init_driver(toggle)

    def set_types(self, general: dict, specialized: dict) -> None:

        self.general_types = general

        self.specialized_types = specialized

    def research(self, links_w_ids: list) -> None:

        self.__open("keep open")

        for set in links_w_ids:

            l = set[1]
            
            self.driver.get(l)

            if l != links_w_ids[-1]:

                self.driver.execute_script("window.open('');")
                chwd = self.driver.window_handles
                self.driver.switch_to.window(chwd[-1])

    def __new_tab(self):

        self.driver.execute_script("window.open('');")
        chwd = self.driver.window_handles
        self.driver.switch_to.window(chwd[-1])

        return chwd[0]
        
    def __check_list_and_int_for_condition(self, list_or_int_var, condition) -> bool:

        if type(list_or_int_var) == int:

            if list_or_int_var == condition:

                return True

        elif type(list_or_int_var) == list:

            for elemt in list_or_int_var:

                if elemt == condition:

                    return True

        return False

    def run_characterization(self) -> list:

        self.__open("keep open")


        id_layout = []

        for set in self.links_w_ids:

            match_found = False

            id = set[0]

            link = set[1]

            self.driver.get(link)

            if id in self.specialized_types:

                id_layout.append([id, self.specialized_types[id].name])

                match_found = True

                print(id, link, self.specialized_types[id].name)

            if not match_found:

                for layout in self.general_types.values():

                    try:
                        article_elements = self.driver.find_elements_by_xpath(layout.xpath)

                        if self.__check_list_and_int_for_condition(layout.count_on_page, len(article_elements)):

                            match_found = True
                    
                    except NoSuchElementException:
                        continue
                    
                    if match_found:

                        print(id, link, layout.name)

                        id_layout.append([id, layout.name])

                        break

            if set != self.links_w_ids[-1]:
                self.__new_tab()

            if match_found:

                chwd = self.driver.window_handles

                self.driver.switch_to.window(chwd[-2])

                self.driver.close()

                chwd = self.driver.window_handles

                self.driver.switch_to.window(chwd[-1])


        print(id_layout)

        return id_layout
