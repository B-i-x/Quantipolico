from selenium import webdriver
from selenium.webdriver.common.by import By



def reformat_name(s: str) -> str:

    if s == "LaHood,Darin(link is external)":
        return "Darin LaHood"

    if s.find("(link is external)") == -1:
        return None

    try:
        s = s.replace("(link is external)", "").replace(",", "")

        s = s.split(" ")

        s = s[1] + " " + s[0]
    except IndexError:
        return None

    return s

def crawl():
    house_directory = 'https://www.house.gov/representatives'
    driver = webdriver.Chrome(executable_path=r"C:\Users\alexr\Documents\Projects\Mathematical Politics\repository\dep\chromedriver_win32\chromedriver.exe")
    driver.get(house_directory)

    data = []

    for state_num in range(1, 56+1):

        state_table_xpath = f'//*[@id="by-state"]/div/div//table[{state_num}]'

        state_name = driver.find_element(By.XPATH, state_table_xpath+"//caption").text

        district_list_elem = driver.find_elements(By.XPATH, state_table_xpath + "//td[1]")

        name_list_elem = driver.find_elements(By.XPATH, state_table_xpath + "//td[2]")

        link_list_elem = driver.find_elements(By.XPATH, state_table_xpath + "//td[2]//a")

        party_list_elem = driver.find_elements(By.XPATH, state_table_xpath + "//td[3]")

        for elem_num in range(len(district_list_elem)):

            name = reformat_name(name_list_elem[elem_num].text)

            data.append([name, state_name, party_list_elem[elem_num].text, district_list_elem[elem_num].text, link_list_elem[elem_num].get_attribute('href')])

    driver.quit()

    return data
    