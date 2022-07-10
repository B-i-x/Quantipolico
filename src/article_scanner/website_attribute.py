class Site_Attribute():

    def __init__(self) -> None:
        
        self.xpath = None

        self.name = None

        self.amount = None

        self.ids = None

        self.attribute_column_name = None

    def if_var_list(self, var) -> bool:

        if type(var) == int:

            return False

        return True

    def if_attribute_limited_to_ids(self) -> bool:

        if self.ids is None:

            return False

        return True

        