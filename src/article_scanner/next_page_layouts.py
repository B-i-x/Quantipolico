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






        
