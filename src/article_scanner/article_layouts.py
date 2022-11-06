from article_scanner.website_attribute import Site_Attribute

class Article_Layout_Structure(Site_Attribute):
    '''this is a class for a general attribute of the website, specifically the article links
    
    a property of this attribute are its child classes'''
    def __init__(self) -> None:
        
        super(Site_Attribute, self).__init__()

        self.attribute_column_name = 'press_release_layout'

A = Site_Attribute()
    

class A(Article_Layout_Structure):

    def __init__(self) -> None:

        super(Article_Layout_Structure, self).__init__()
        
        self.name = 'find_press_release_first'

        self.xpath = '//*[text()="Press Release"]//ancestor::div[1]/div[1]//a'

        self.amount = 10
        
            
class B(Article_Layout_Structure):

    def __init__(self) -> None:
        
        super().__init__()

        self.name = 'table'

        self.xpath = "//table//a"

        self.amount = 10


class C(Article_Layout_Structure):

    def __init__(self) -> None:

        super().__init__()

        self.name = "read_more"

        self.xpath = "//a[contains(text(),'Read more')]"

        self.amount = 10   


class D(Article_Layout_Structure):

    def __init__(self) -> None:
        
        super().__init__()

        self.name = "newsie"

        self.xpath = '//h2[@class="newsie-titler"]//a'

        self.amount = 10


class E(Article_Layout_Structure):

    def __init__(self) -> None:

        super().__init__()

        self.name = "find_press_release_first_modification_div[1->4]"

        self.xpath = '//*[text()="Press Release"]//ancestor::div[4]/div[1]//a'

        self.amount = [10, 25, 100]

        
class F(Article_Layout_Structure):

    def __init__(self) -> None:

        super().__init__()

        self.name = "read_more_modification_InitialCaps"

        self.xpath = "//a[contains(text(),'Read More')]"

        self.amount = [10, 15, 18]

        
class D(Article_Layout_Structure):

    def __init__(self) -> None:

        super().__init__()

        self.name = "continue_reading_InitialCaps"

        self.xpath = "//a[contains(text(),'Continue')]"

        self.amount = 20


class E(Article_Layout_Structure):

    def __init__(self) -> None:

        super().__init__()

        self.name = "sablan"

        self.xpath = '//div[@class="list-item"]'

        self.amount = 10

        self.ids = 302


class F(Article_Layout_Structure):
    '''for nancy pelosi'''
    def __init__(self) -> None:

        super().__init__()

        self.name = "nancy"

        self.xpath = "//*[contains(text(),'Press Release')]/parent::div//a[contains(text(),'Press Release')]//ancestor::div[1]/div[1]//a"

        self.amount = 10

        self.ids = 34
    

class G(Article_Layout_Structure):
    '''for nancy pelosi'''
    def __init__(self) -> None:

        super().__init__()

        self.name = "read_more_modification_ALLCAPS"

        self.xpath = "//a[contains(text(),'READ MORE')]"

        self.amount = 10
            

class H(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "date_div_1"

        self.xpath = "//*[contains(text(), 'Jan') or contains(text(), 'Feb') or contains(text(), 'Mar') or  contains(text(), 'Apr') or contains(text(), 'May') or contains(text(), 'Jun') or contains(text(), 'Jul') or contains(text(), 'Aug') or contains(text(), 'Sep') or contains(text(), 'Oct') or contains(text(), 'Nov') or contains(text(), 'Dec')]/ancestor::div[1]//a"

        self.amount = 10


class I(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "date_div_2"

        self.xpath = "//*[contains(text(), 'Jan') or contains(text(), 'Feb') or contains(text(), 'Mar') or  contains(text(), 'Apr') or contains(text(), 'May') or contains(text(), 'Jun') or contains(text(), 'Jul') or contains(text(), 'Aug') or contains(text(), 'Sep') or contains(text(), 'Oct') or contains(text(), 'Nov') or contains(text(), 'Dec')]/ancestor::div[2]//a"

        self.amount = [10, 11, 25]


class J(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "click_here_to_read_the_full_news_release"

        self.xpath = "//a[contains(text(),'Click here to read the full news release')]"

        self.amount = 10

        self.ids = 119


class K(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "more"

        self.xpath = "//a[contains(text(),'More')]"

        self.amount = 10


class L(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "find_press_release_first_modification_two_more_divs"

        self.xpath = "//*[text()='Press Release']/ancestor::div[4]/div[1]//div[1]/div/div//a"

        self.amount = 20

        self.ids = 31


class M(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "find_press_release_first_modification_news_release"

        self.xpath = "//*[text()='News Releases']/ancestor::div[1]/div[1]//a"

        self.amount = 10


class N(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "read_more_modification_go_to_parent"

        self.xpath = "//*[contains(text(),'Read More')]//parent::a"

        self.amount = [20, 6]

        self.ids = [11, 269]


class O(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "table_modification_no_attachments"

        self.xpath = "//table//a[1]"

        self.amount = [10, 15]


class P(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "see_more"

        self.xpath = "//*[text()='See More']//ancestor::a"

        self.amount = 6

        self.ids = [148, 138, 19, 111, 316, 275, 424, 388, 321, 406, 414]


class Q(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "find_press_release_first_modification_uses_headings"

        self.xpath = "//a[text()='Press Releases']//ancestor::div[1]//h2//a"

        self.amount = 10


class U(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "date_div_2_modification_uses_headings"

        self.xpath = "//*[contains(text(), 'Jan') or contains(text(), 'Feb') or contains(text(), 'Mar') or  contains(text(), 'Apr') or contains(text(), 'May') or contains(text(), 'Jun') or contains(text(), 'Jul') or contains(text(), 'Aug') or contains(text(), 'Sep') or contains(text(), 'Oct') or contains(text(), 'Nov') or contains(text(), 'Dec')]/ancestor::div[1]//h2//a"

        self.amount = [4,10]


class R(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "date_div_2_modification_uses_class_name_body"

        self.xpath = "//*[contains(text(), 'Jan') or contains(text(), 'Feb') or contains(text(), 'Mar') or  contains(text(), 'Apr') or contains(text(), 'May') or contains(text(), 'Jun') or contains(text(), 'Jul') or contains(text(), 'Aug') or contains(text(), 'Sep') or contains(text(), 'Oct') or contains(text(), 'Nov') or contains(text(), 'Dec')]/ancestor::div[2]//a[@class='media-digest-body-link']"

        self.amount = 10

        self.ids = 86


class S(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "date_div_2_modification_uses_heading_3"

        self.xpath = "//*[contains(text(), 'Jan') or contains(text(), 'Feb') or contains(text(), 'Mar') or  contains(text(), 'Apr') or contains(text(), 'May') or contains(text(), 'Jun') or contains(text(), 'Jul') or contains(text(), 'Aug') or contains(text(), 'Sep') or contains(text(), 'Oct') or contains(text(), 'Nov') or contains(text(), 'Dec')]/ancestor::div[1]//h3/a"

        self.amount = 10


class T(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "date_div_2_modification_uses_heading_3_div[1->3]"

        self.xpath = "//*[contains(text(), 'Jan') or contains(text(), 'Feb') or contains(text(), 'Mar') or  contains(text(), 'Apr') or contains(text(), 'May') or contains(text(), 'Jun') or contains(text(), 'Jul') or contains(text(), 'Aug') or contains(text(), 'Sep') or contains(text(), 'Oct') or contains(text(), 'Nov') or contains(text(), 'Dec')]/ancestor::div[3]//h3//a"

        self.amount = 10


class V(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "date_div_2_modification_uses_spans"

        self.xpath = "//*[contains(text(), 'Jan') or contains(text(), 'Feb') or contains(text(), 'Mar') or  contains(text(), 'Apr') or contains(text(), 'May') or contains(text(), 'Jun') or contains(text(), 'Jul') or contains(text(), 'Aug') or contains(text(), 'Sep') or contains(text(), 'Oct') or contains(text(), 'Nov') or contains(text(), 'Dec')]//ancestor::table[1]//span//span//a"

        self.amount = 10


class X(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "cicilline"

        self.xpath = "//*[@id='inner-content']/div/h4/a"

        self.amount = 10

        self.ids = 348


class Y(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "jcurtis"

        self.xpath = "//*[@id='archiveView']/div/div/a[2]"

        self.amount = 12

        self.ids = 405


class Z(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "jayapal"

        self.xpath = "//*[@id='main']//article[1]//header/h2/a"

        self.amount = 6

        self.ids = 426


class AA(Article_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "mooney"

        self.xpath = "/html/body//main//article/a"

        self.amount = 9

        self.ids = 431
