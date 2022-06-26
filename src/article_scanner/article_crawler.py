from webdriver_interface import WebDriver_Interface
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

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

         
        
class Article_Layout_Structure():

    def __init__(self, name: str, article_xpath: str, amount: int, ids: int = None) -> None:
        self.name = name

        self.article_xpath = article_xpath

        self.count_on_page = amount

        self.specialized = False

        if ids is not None:
            self.ids = ids

            self.specialized = True


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

        article_xpath = '//*[text()="Press Release"]//ancestor::div[4]/div[1]//a'

        article_count_on_page = [10, 25, 100]

        super().__init__(name, article_xpath, article_count_on_page)

class F(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "read_more_modification_InitialCaps"

        article_xpath = "//a[contains(text(),'Read More')]"

        article_count_on_page = [10, 15, 18]

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

class F(Article_Layout_Structure):
    '''for nancy pelosi'''
    def __init__(self) -> None:

        name = "nancy"

        article_xpath = "//*[contains(text(),'Press Release')]/parent::div//a[contains(text(),'Press Release')]//ancestor::div[1]/div[1]//a"

        amount = 10

        ids = 34

        super().__init__(name, article_xpath, amount, ids)

class G(Article_Layout_Structure):
    '''for nancy pelosi'''
    def __init__(self) -> None:

        name = "read_more_modification_ALLCAPS"

        article_xpath = "//a[contains(text(),'READ MORE')]"

        amount = 10
        
        super().__init__(name, article_xpath, amount)

class H(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "date_div_1"

        article_xpath = "//*[contains(text(), 'Jan') or contains(text(), 'Feb') or contains(text(), 'Mar') or  contains(text(), 'Apr') or contains(text(), 'May') or contains(text(), 'Jun') or contains(text(), 'Jul') or contains(text(), 'Aug') or contains(text(), 'Sep') or contains(text(), 'Oct') or contains(text(), 'Nov') or contains(text(), 'Dec')]/ancestor::div[1]//a"

        amount = 10
        super().__init__(name, article_xpath, amount)

class I(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "date_div_2"

        article_xpath = "//*[contains(text(), 'Jan') or contains(text(), 'Feb') or contains(text(), 'Mar') or  contains(text(), 'Apr') or contains(text(), 'May') or contains(text(), 'Jun') or contains(text(), 'Jul') or contains(text(), 'Aug') or contains(text(), 'Sep') or contains(text(), 'Oct') or contains(text(), 'Nov') or contains(text(), 'Dec')]/ancestor::div[2]//a"

        amount = [10, 11, 25]

        super().__init__(name, article_xpath, amount)

class J(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "click_here_to_read_the_full_news_release"

        article_xpath = "//a[contains(text(),'Click here to read the full news release')]"

        amount = 10

        ids = 119

        super().__init__(name, article_xpath, amount, ids)

class K(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "more"

        article_xpath = "//a[contains(text(),'More')]"

        amount = 10

        super().__init__(name, article_xpath, amount)

class L(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "find_press_release_first_modification_two_more_divs"

        article_xpath = "//*[text()='Press Release']/ancestor::div[4]/div[1]//div[1]/div/div//a"

        amount = 20

        ids = 31

        super().__init__(name, article_xpath, amount, ids)

class M(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "find_press_release_first_modification_news_release"

        article_xpath = "//*[text()='News Releases']/ancestor::div[1]/div[1]//a"

        amount = 10

        super().__init__(name, article_xpath, amount)

class N(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "read_more_modification_go_to_parent"

        article_xpath = "//*[contains(text(),'Read More')]//parent::a"

        amount = [20, 6]

        ids = [11, 269]

        super().__init__(name, article_xpath, amount, ids)

class O(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "table_modification_no_attachments"

        article_xpath = "//table//a[1]"

        amount = [10, 15]

        super().__init__(name, article_xpath, amount)

class P(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "see_more"

        article_xpath = "//*[text()='See More']//ancestor::a"

        amount = 6

        ids = [148, 138, 19, 111, 316, 275, 424, 388, 321, 406, 414]

        super().__init__(name, article_xpath, amount, ids)

class Q(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "find_press_release_first_modification_uses_headings"

        article_xpath = "//a[text()='Press Releases']//ancestor::div[1]//h2//a"

        amount = 10

        super().__init__(name, article_xpath, amount)

class U(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "date_div_2_modification_uses_headings"

        article_xpath = "//*[contains(text(), 'Jan') or contains(text(), 'Feb') or contains(text(), 'Mar') or  contains(text(), 'Apr') or contains(text(), 'May') or contains(text(), 'Jun') or contains(text(), 'Jul') or contains(text(), 'Aug') or contains(text(), 'Sep') or contains(text(), 'Oct') or contains(text(), 'Nov') or contains(text(), 'Dec')]/ancestor::div[1]//h2//a"

        amount = [4,10]

        super().__init__(name, article_xpath, amount)

class R(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "date_div_2_modification_uses_class_name_body"

        article_xpath = "//*[contains(text(), 'Jan') or contains(text(), 'Feb') or contains(text(), 'Mar') or  contains(text(), 'Apr') or contains(text(), 'May') or contains(text(), 'Jun') or contains(text(), 'Jul') or contains(text(), 'Aug') or contains(text(), 'Sep') or contains(text(), 'Oct') or contains(text(), 'Nov') or contains(text(), 'Dec')]/ancestor::div[2]//a[@class='media-digest-body-link']"

        amount = 10

        ids = 86

        super().__init__(name, article_xpath, amount, ids)

class S(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "date_div_2_modification_uses_heading_3"

        article_xpath = "//*[contains(text(), 'Jan') or contains(text(), 'Feb') or contains(text(), 'Mar') or  contains(text(), 'Apr') or contains(text(), 'May') or contains(text(), 'Jun') or contains(text(), 'Jul') or contains(text(), 'Aug') or contains(text(), 'Sep') or contains(text(), 'Oct') or contains(text(), 'Nov') or contains(text(), 'Dec')]/ancestor::div[1]//h3/a"

        amount = 10

        super().__init__(name, article_xpath, amount)

class T(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "date_div_2_modification_uses_heading_3_div[1->3]"

        article_xpath = "//*[contains(text(), 'Jan') or contains(text(), 'Feb') or contains(text(), 'Mar') or  contains(text(), 'Apr') or contains(text(), 'May') or contains(text(), 'Jun') or contains(text(), 'Jul') or contains(text(), 'Aug') or contains(text(), 'Sep') or contains(text(), 'Oct') or contains(text(), 'Nov') or contains(text(), 'Dec')]/ancestor::div[3]//h3//a"

        amount = 10

        super().__init__(name, article_xpath, amount)

class V(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "date_div_2_modification_uses_spans"

        article_xpath = "//*[contains(text(), 'Jan') or contains(text(), 'Feb') or contains(text(), 'Mar') or  contains(text(), 'Apr') or contains(text(), 'May') or contains(text(), 'Jun') or contains(text(), 'Jul') or contains(text(), 'Aug') or contains(text(), 'Sep') or contains(text(), 'Oct') or contains(text(), 'Nov') or contains(text(), 'Dec')]//ancestor::table[1]//span//span//a"

        amount = 10

        super().__init__(name, article_xpath, amount)