from selenium import webdriver
from selenium.webdriver.common.by import By

def crawl():
    house_directory = 'https://www.google.com/'
    driver = webdriver.Chrome(executable_path=r"C:\Users\alexr\Documents\Projects\Mathematical Politics\repository\dep\chromedriver_win32\chromedriver.exe")
    driver.get(house_directory)