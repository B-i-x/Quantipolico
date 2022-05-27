
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebDriver_Interface:

    def __init__(self, link=None):
        pass

    def init_driver(self):
        p = r"C:\Users\alexr\Documents\Projects\Mathematical Politics\repository\dep\chromedriver_win32\chromedriver.exe"

        driver = webdriver.Chrome(executable_path=p)

        return driver
    

class PressRelease_Scanner:

    def __init__(self, debug = False) -> None:
        '''names is a tuple from DataTable.select_col_from_table'''
        self.driver = WebDriver_Interface()

        self.curr_name = self.return_link = None

        self.first_website_flag = True #false means the website is not on its first one and true means it is

        self.failure = False

        self.debug = debug

        self.__open()
    
    def run(self) -> None:
        
        search_bar_xpath = self.__get_search_bar_xpath()

        self.failure = self.__get_individual_link(self.curr_name, search_bar_xpath)

        self.first_website_flag = False

        if self.debug:
            print(self.return_link)

        if self.failure:
            self.__quit()
        
    def set_name(self, name: str) -> None:

        self.curr_name = name

    def __get_individual_link(self, name: str, search_bar_xpath: str) -> bool:
        '''gets the press release link from the page on google of the given person's name'''

        try:
            searchBar = self.driver.find_element(By.XPATH, search_bar_xpath)

        except NoSuchElementException:
            return False

        searchBar.clear()

        type_in = name + " press releases"

        a3 = webdriver.ActionChains(self.driver)
        a3.move_to_element(searchBar).click().send_keys(type_in, Keys.ENTER).perform()

        first_link_xpath = r'//div[@id="rso"]//div//a'

        first_link_present = EC.presence_of_all_elements_located((By.XPATH, first_link_xpath))

        WebDriverWait(self.driver, timeout=5).until(first_link_present)

        first_link = self.driver.find_element(By.XPATH, first_link_xpath) 

        self.return_link = first_link.get_attribute("href")

    def get_link(self) -> str:
        """returns link for that name"""
        
        return self.return_link

    def __open(self) ->None:
        
        self.driver = self.driver.init_driver()

        self.driver.get("https://www.google.com/")
    
    def __quit(self) -> None:

        self.driver.close()

    def __get_search_bar_xpath(self) -> str:

        if self.first_website_flag:
            return '//body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
        
        return '//div[@ID="searchform"]//input[1]'



def get_link_for_individual(driver, name: str, last = False, first = False) -> str:

    searchBar_xpath = ""
    if first:
        searchBar_xpath = "//body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"

    else:
        searchBar_xpath = '//div[@ID="searchform"]//input[1]'

    searchBar = driver.find_element(By.XPATH, searchBar_xpath)

    searchBar.clear()

    a3 = webdriver.ActionChains(driver)
    a3.move_to_element(searchBar).click().send_keys(name + " press releases", Keys.ENTER).perform()

    first_link_xpath = r'//div[@id="rso"]//div//a'

    first_link_present = EC.presence_of_all_elements_located((By.XPATH, first_link_xpath))

    WebDriverWait(driver, timeout=5).until(first_link_present)

    first_link = driver.find_element(By.XPATH, first_link_xpath) 

    press_releases_link = first_link.get_attribute("href")

    if last:
        driver.quit()

    return press_releases_link

def search(webdriver_obj, tup_names: list) -> list:

    links = []

    names_str = ["".join(n) for n in tup_names]

    for name in names_str:
        link = ""
        if name == names_str[-1]:
            link = get_link_for_individual(webdriver_obj, name, last=True)
        elif name == names_str[0]:
            link = get_link_for_individual(webdriver_obj, name, first=True)
        else:
            link = get_link_for_individual(webdriver_obj, name)

        links.append(link)

    return links