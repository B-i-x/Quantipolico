
from platform import release
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

    a3 = webdriver.ActionChains(driver)
    a3.move_to_element(searchBar).click().send_keys(name + " press releases", Keys.ENTER).perform()

    driver.implicitly_wait(10)

    first_link_xpath = '//*[@id="rso"]/div[1]/div/div[1]/div[1]/a'

    first_link = driver.find_element(By.XPATH, first_link_xpath) 

    press_releases_link = first_link.get_attribute("href")

    if last:
        driver.quit()

    searchBar_xpath = '//div[@ID="searchform"]//input[1]'

    searchBar = driver.find_element(By.XPATH, searchBar_xpath)

    a1 = webdriver.ActionChains(driver)
    a1.move_to_element(searchBar).click().key_down(Keys.CONTROL).send_keys("A").perform()

    a2 = webdriver.ActionChains(driver)
    a2.send_keys(Keys.BACKSPACE)

    return press_releases_link
