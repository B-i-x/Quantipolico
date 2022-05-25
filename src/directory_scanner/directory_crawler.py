from selenium import webdriver
from selenium.webdriver.common.by import By



def reformat_name(s: str) -> str:

    if s.find("(link is external)") == -1:
        return None

    try:
        s = s.replace("(link is external)", "").replace(",", "")

        s = s.split(" ")

        s = s[1] + " " + s[0]
    except IndexError:
        return None

    return s

def reformat_district(s: str) -> int:
    
    if s == "At Large" or s == "Delegate" or s == "Resident Commissioner":
        return 1

    i = s[:-2]
    return int(i)

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

            link = link_list_elem[elem_num].get_attribute('href')

            district_num = reformat_district(district_list_elem[elem_num].text)

            data.append([name, state_name, party_list_elem[elem_num].text, district_num, link])

    driver.quit()

    print(data)

    return data
    