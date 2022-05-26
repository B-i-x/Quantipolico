
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Crawler:

    
    def __init__(self, link):
        self.l = link
        self.p = r"C:\Users\alexr\Documents\Projects\Mathematical Politics\repository\dep\chromedriver_win32\chromedriver.exe"

    def start(self):
        driver = webdriver.Chrome(executable_path= self.p)
        driver.get(self.l)

        return driver

def search(driver, name: str, last = False, first = False) -> str:

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
