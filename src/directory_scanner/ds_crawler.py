from selenium import webdriver
from selenium.webdriver.common.by import By

from representative_class import reformat_name
from src.webdriver_interface import WebDriver_Interface

class Directory_Scanner:

    def __init__(self) -> None:
        self.driver = WebDriver_Interface()

        self.__open()

        self.names = self.links = self.parties = self.states = self.districts = []

    def __open(self) ->None:
        
        self.driver = self.driver.init_driver()

        self.driver.get('https://www.house.gov/representatives')

    def run(self) -> None:
        

        for state_num in range(1, 56+1):
            state_table_xpath = f'//*[@id="by-state"]/div/div//table[{state_num}]'

            data_search_order = [
                "name",
                "link",
                "party",
                "district",
            ]

            state_name = self.driver.find_elements(By.XPATH, state_table_xpath + self.get_addition_for("state_name", return_type="XPATH"))

            for type_of_data in data_search_order:

                data_elem_list = self.driver.find_elements(By.XPATH, state_table_xpath + self.get_addition_for(type_of_data, return_type="XPATH"))

                self.get_addition_for(type_of_data, "LIST").extend(data_elem_list)

        
    def get_addition_for(self, data: str, return_type: str):
        xpath = None
        
        return_list = []

        if data == "district":
            xpath = "//td[1]"
            return_list = self.districts

        elif data == "name":
            xpath = "//td[2]"
            return_list = self.names

        elif data == "link":
            xpath = "//td[2]//a"
            return_list = self.links

        elif data == "party":
            xpath = "//td[3]"
            return_list = self.parties

        elif data == "state_name":
            xpath = "//caption"
            return_list = self.states
        else:
            print("UNRECOGNIZED DATA TYPE TO SEARCH FOR")
            return

        if return_type == "XPATH":
            return xpath
        elif return_type == "LIST":
            return return_list
        else: 
            print("UNRECOGNIZED RETURN VALUE")
            return


def crawl(refresh_name: bool = False):
    house_directory = 'https://www.house.gov/representatives'
    driver = webdriver.Chrome(executable_path=r"C:\Users\alexr\Documents\Projects\Mathematical Politics\repository\dep\chromedriver_win32\chromedriver.exe")
    driver.get(house_directory)

    data = []

    for state_num in range(1, 56+1):

        state_table_xpath = f'//*[@id="by-state"]/div/div//table[{state_num}]'

        if refresh_name():
            
            names = []

            for elem_num in range(len(district_list_elem)):

                name = reformat_name(name_list_elem[elem_num].text)

                names.append(name)

            driver.quit()

            return names

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
    