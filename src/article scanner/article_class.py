
class article():

    def __init__(self):
        self.title = self.content = None
        
        self.day = self.month = self.year = None

    def get_length(self) -> int:

        return self.calculate_length()

        