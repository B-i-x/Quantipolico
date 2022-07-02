class Next_Layout_Structure():

    def __init__(self, next_button_xpath: str, name: str, ids: int = None) -> None:

        self.next_button_xpath = next_button_xpath

        self.name = name
        
        self.specialized = False

        if ids is not None:
            self.ids = ids

            self.specialized = True

class A(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "next_arrow"

        xpath = "//a[text()='next ›']"

        super.__init__(xpath, name)

class B(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "double_arrow"

        xpath = "//a[@title='Go to next page']"

        super.__init__(xpath, name)

class C(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "Next_double_arrow"

        xpath = "//a[text()='Next »']"

        super.__init__(xpath, name)

class D(Next_Layout_Structure):

    def __init__(self) -> None:

        name = "Next_arrow"

        xpath = "//a[text()='Next >']"

        super.__init__(xpath, name)
        
