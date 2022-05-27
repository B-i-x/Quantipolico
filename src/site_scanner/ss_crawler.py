
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebDriver_Interface:
    
    def __init__(self, link=None):
        self.link = link

    def __new__(cls, link=None):
      
        p = r"C:\Users\alexr\Documents\Projects\Mathematical Politics\repository\dep\chromedriver_win32\chromedriver.exe"
        driver = webdriver.Chrome(executable_path= p)

        return driver

class PressRelease_Scanner:

    def __init__(self, names: list) -> None:
        '''names is a tuple from DataTable.select_col_from_table'''
        self.driver = WebDriver_Interface()

        self.names = [["".join(n) for n in names]]

        self.return_at_count = None

        self.nested_data = []

        self.first_website_flag = True #false means the website is not on its first one and true means it is

    
    def run(self) -> None:

        if self.return_at_count is None:
            print("Set a return count first!")
            return
        
        self.__refresh()

        return_count = 0

        links_list = []

        for name in self.names:

            if return_count == self.return_at_count:

                self.nested_data.append(links_list)

                links_list.clear()

                self.__refresh()

                self.first_website_flag = True

            #this is where the code execution goes\/\/\/

            links_list.append(self.__get_individual_link(name, self.__get_search_bar_xpath))

            return_count += 1

            self.first_website_flag = False

    def __get_individual_link(self, name: str, search_bar_xpath: str) -> str:

        searchBar = self.driver.find_element(By.XPATH, search_bar_xpath)

        searchBar.clear()

        a3 = webdriver.ActionChains(self.driver)
        a3.move_to_element(searchBar).click().send_keys(name + " press releases", Keys.ENTER).perform()

        first_link_xpath = r'//div[@id="rso"]//div//a'

        first_link_present = EC.presence_of_all_elements_located((By.XPATH, first_link_xpath))

        WebDriverWait(self.driver, timeout=5).until(first_link_present)

        first_link = self.driver.find_element(By.XPATH, first_link_xpath) 

        press_releases_link = first_link.get_attribute("href")

        return press_releases_link

    def get_data(self) -> list:
        """returns unnested self.data"""

        d = []

        for group in self.nested_data:

            for link in group:
                d.append(link)

        return d

    def __refresh(self) ->None:

        if not self.first_website_flag:
            self.driver.quit()

        self.driver.get("https://www.google.com/")

    def __get_search_bar_xpath(self) -> str:

        if self.first_website_flag:
            return '//body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
        
        return '//div[@ID="searchform"]//input[1]'

    def set_return_at_count(self, i: int):
        self.return_at_count = i

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