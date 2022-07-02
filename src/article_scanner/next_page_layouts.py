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

class D(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "See_More"

        xpath = "//*[text()='See More' and not(ancestor::a)]"

        ids = [148, 138, 19, 111, 316, 275, 424, 388, 321, 406, 414]

        super().__init__(xpath, name, ids)


        
