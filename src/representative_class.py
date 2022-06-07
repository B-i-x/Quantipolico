
class rep: 
    '''every single person in congress has an
    homepage - link to the home page
    name - name of the person with first letters of first and last name in caps (John Doe)
    state - name of state (eg. Arizona, Puerto Rice) ik Pr is not state but i will call it that
    party - R or D or I
    district - number 1-x
    '''
    def __init__(self) -> None:
        pass

def reformat_name(s: str) -> str:
    """this reformats the crawled names into their database names"""  

    if s.find("(link is external)") == -1:
        return None
        

    try:
        s = s.replace("(link is external)", "").replace("'", "").replace(".", "").replace("-", "")

        s = s.split(",")

        f = ""
        for n in range(len(s)):

            f = f + s[-(n+1)]
        
    except IndexError:
        return None

    f = f.replace(" ", "")

    return f


