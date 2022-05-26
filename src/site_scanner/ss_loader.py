from site_scanner.ss_crawler import search

def get_names():
    pass

def load_pressReleases_sites(database_connection, load: str):
    '''this checks whether each representative has a press release website
    
    get names from directory table'''

    if load == "hard":
        search("Jerry Carl")
        #do some crawling
        pass
    elif load == "light":
        #checks that they all exist, a.k.a stupid validation 
        pass

def load_individuals(database_connection, load: str):
    '''makes all the tables for the 441 people of congress + ur mom'''
    if load == "hard":
       
        #create them for the first time
        pass
    elif load == "light":
        #checks that they all exist, a.k.a stupid validation 
        pass
