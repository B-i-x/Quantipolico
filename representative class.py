class rep: 
    '''every single person in congress has an
    homepage - link to the home page
    name - name of the person with first letters of first and last name in caps (John Doe)
    state - name of state (eg. Arizona, Puerto Rice) ik Pr is not state but i will call it that
    party - R or D or I
    district - number 1-x
    '''
    def __init__(self, homepage, name, state, party, district):
        self.home = homepage

        self.name = name

        self.stte = state

        self.pty = party

        self.dtct = district

        self.create_artice_list()

    def create_artice_list(self):
        '''creates the list of links for each person'''
        self.lart = []

    def set_press_release_homepage(self, press_release_homepage):
        '''this is the link to where all the press releases are stored'''
        self.prhm = press_release_homepage

    def set_id(self, i):
        self.id = i

class artcle(rep):

    def __init__(self, Title, date, length, content):
        pass