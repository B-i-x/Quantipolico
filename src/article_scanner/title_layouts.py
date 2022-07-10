from matplotlib.pyplot import title
from article_scanner.website_attribute import Site_Attribute

class Title_Layout_Structure(Site_Attribute):

     def __init__(self, name: str, title_xpath: str, amount: int, ids = None) -> None:
        
        super().__init__(title_xpath, name, amount, ids)

        self.attribute_column_name = 'title_layout'
        

    