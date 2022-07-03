class Next_Layout_Structure():

    def __init__(self, next_button_xpath: str, name: str, ids: int = None) -> None:

        self.xpath = next_button_xpath

        self.name = name

        self.count_on_page = 1
        
        self.specialized = False

        if ids is not None:
            self.ids = ids

            self.specialized = True

class A(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "next_arrow"

        xpath = "//a[text()='next ›']"

        super().__init__(xpath, name)

class B(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "double_arrow"

        xpath = "//a[@title='Go to next page']"

        super().__init__(xpath, name)

class C(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "Next_double_arrow"

        xpath = "//a[text()='Next »']"

        super().__init__(xpath, name)

class D(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "Next_arrow"

        xpath = "//a[text()='Next >']"

        super().__init__(xpath, name)

class E(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "See_More"

        xpath = "//*[text()='See More' and not(ancestor::a)]"

        ids = [148, 138, 19, 111, 316, 275, 424, 388, 321, 406, 414]

        super().__init__(xpath, name, ids)

class F(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "arrow"

        xpath = "//a[text()='›']"

        super().__init__(xpath, name)

class G(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "Next"

        xpath = "//a[text()='Next']"

        super().__init__(xpath, name)

class H(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "Next_big_arrow"

        xpath = "//a[text()='Next ›']"

        super().__init__(xpath, name)

class I(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "next_double_arrow"

        xpath = "//a[text()='next ›']"

        super().__init__(xpath, name)

class J(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "contains_next"

        xpath = "//a[contains(text(),'next')]"

        super().__init__(xpath, name)

class K(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "stupid_svg"

        xpath = "//a[@aria-label='Next']"

        ids = 405

        super().__init__(xpath, name, ids=ids)

class L(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "double_small_arrow"

        xpath = "//a[text()='»']"

        super().__init__(xpath, name)

class M(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "next_page_label"

        xpath = "//a[@aria-label='Next Page']"

        super().__init__(xpath, name)


class N(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "single_page_no_next_button"

        xpath = ""

        ids = 11

        super().__init__(xpath, name, ids=ids)

class O(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "more_than_brownley"

        xpath = "//a[@class='next page-numbers' and text()='>']"

        ids = 48

        super().__init__(xpath, name, ids=ids)

class P(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "double_next"

        xpath = "//a[text()='Next']"

        ids = [127, 97]

        super().__init__(xpath, name, ids=ids)

        self.count_on_page = 2

class Q(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "page_arrow_maloney"

        xpath = "//a[text()='page ›']"

        ids = 272

        super().__init__(xpath, name, ids=ids)

class R(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "Next_Page_Mooney"

        xpath = "//a[text()='Next Page']"

        ids = 431

        super().__init__(xpath, name, ids=ids)

class S(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "cheney"

        xpath = "//a[@aria-label='next arrow']"

        ids = 441

        super().__init__(xpath, name, ids=ids)



        
