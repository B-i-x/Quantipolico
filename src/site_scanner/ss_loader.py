from site_scanner.ss_crawler import search

from site_scanner.ss_crawler import Crawler

def reformat_sql_query_result(s: str) -> str:

    s.replace("('").replace("")


def validate_pressReleases_sites(directory_tbl):
    '''this checks whether each representative has a press release website
    
    get names from directory table'''

    press_releases = 1 #check the directory table and do real validation

    if press_releases == 1:

        names = directory_tbl.select_col_from_table("name")

        crawler_obj = Crawler('https://www.google.com/')

        d = crawler_obj.start()

        for n in names:
            name = "".join(n) #convert tuple to string

            l = ""
            if n == names[-1]:
                l = search(d, name, last=True)
            elif n == names[0]:
                l = search(d, name, first=True)
            else:
                l = search(d, name)

            print(l)
            

        #link = search("Jerry Carl")
        #do some crawling
    

def load_individuals(database_connection, load: str):
    '''makes all the tables for the 441 people of congress + ur mom'''
    if load == "hard":
       
        #create them for the first time
        pass
    elif load == "light":
        #checks that they all exist, a.k.a stupid validation 
        pass
