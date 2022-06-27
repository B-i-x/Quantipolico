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

class X(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "cicilline"

        article_xpath = "//*[@id='inner-content']/div/h4/a"

        amount = 10

        ids = 348

        super().__init__(name, article_xpath, amount, ids)

class Y(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "jcurtis"

        article_xpath = "//*[@id='archiveView']/div/div/a[2]"

        amount = 12

        ids = 405

        super().__init__(name, article_xpath, amount, ids)

class Z(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "jayapal"

        article_xpath = "//*[@id='main']//article[1]//header/h2/a"

        amount = 6

        ids = 426

        super().__init__(name, article_xpath, amount, ids)

class AA(Article_Layout_Structure):

    def __init__(self) -> None:

        name = "mooney"

        article_xpath = "/html/body//main//article/a"

        amount = 9

        ids = 431

        super().__init__(name, article_xpath, amount, ids)