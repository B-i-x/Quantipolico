from article_scanner.website_attribute import Site_Attribute


class Next_Layout_Structure(Site_Attribute):

    def __init__(self) -> None:

        super().__init__()

        self.amount = 1

        self.attribute_column_name = 'next_page_control'


class A(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "next_arrow"

        self.xpath = "//a[text()='next ›']"


class B(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "double_arrow"

        self.xpath = "//a[@title='Go to next page']"


class C(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "Next_double_arrow"

        self.xpath = "//a[text()='Next »']"


class D(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "Next_arrow"

        self.xpath = "//a[text()='Next >']"


class E(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "See_More"

        self.xpath = "//*[text()='See More' and not(ancestor::a)]"

        self.ids = [148, 138, 19, 111, 316, 275, 424, 388, 321, 406, 414]


class F(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "arrow"

        self.xpath = "//a[text()='›']"


class G(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "Next"

        self.xpath = "//a[text()='Next']"


class H(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "Next_big_arrow"

        self.xpath = "//a[text()='Next ›']"


class I(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "next_double_arrow"

        self.xpath = "//a[text()='next ›']"


class J(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "contains_next"

        self.xpath = "//a[contains(text(),'next')]"


class K(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "stupid_svg"

        self.xpath = "//a[@aria-label='Next']"

        self.ids = 405


class L(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "double_small_arrow"

        self.xpath = "//a[text()='»']"


class M(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "next_page_label"

        self.xpath = "//a[@aria-label='Next Page']"



class N(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "single_page_no_next_button"

        self.xpath = ""

        self.ids = 11


class O(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "more_than_brownley"

        self.xpath = "//a[@class='next page-numbers' and text()='>']"

        self.ids = 48


class P(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "double_next"

        self.xpath = "//a[text()='Next']"

        self.ids = [127, 97]

        self.amount = 2


class Q(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "page_arrow_maloney"

        self.xpath = "//a[text()='page ›']"

        self.ids = 272


class R(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "Next_Page_Mooney"

        self.xpath = "//a[text()='Next Page']"

        self.ids = 431


class S(Next_Layout_Structure):

    def __init__(self) -> None:
        super().__init__()

        self.name = "cheney"

        self.xpath = "//a[@aria-label='next arrow']"

        self.ids = 441




        
