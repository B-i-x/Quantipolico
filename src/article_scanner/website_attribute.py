class Site_Attribute():

    def __init__(self, xpath: str, name : str, amount, ids = None) -> None:
        
        self.xpath = xpath

        self.name = name

        self.amount = amount

        self.ids = ids

        self.attribute_column_name = None

    def if_var_list(self, var) -> bool:

        if type(var) == int:

            return False

        return True

    def if_attribute_limited_to_ids(self) -> bool:

        if self.ids is None:

            return False

        return True

        