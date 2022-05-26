
from platform import release
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def search(name: str) -> str:
    house_directory = 'https://www.google.com/'
    driver = webdriver.Chrome(executable_path=r"C:\Users\alexr\Documents\Projects\Mathematical Politics\repository\dep\chromedriver_win32\chromedriver.exe")
    driver.get(house_directory)

    searchBar_xpath = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"

    action = webdriver.ActionChains(driver)

    searchBar = driver.find_element(By.XPATH, searchBar_xpath)

    action.move_to_element(searchBar).click().send_keys(name + "press releases", Keys.ENTER).perform()

    first_link_xpath = '//*[@id="rso"]/div[1]/div/div[1]/div[1]/a'

    first_link = driver.find_element(By.XPATH, first_link_xpath) 

    press_releases_link = first_link.get_attribute("href")

    print(press_releases_link)

    return press_releases_link

    driver.quit()