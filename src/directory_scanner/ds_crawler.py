from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

from representative_class import reformat_name
from webdriver_interface import WebDriver_Interface

class Directory_Scanner:

    def __init__(self) -> None:
        self.driver = WebDriver_Interface()

        self.__open()

        self.names = self.links = self.parties = self.states = self.districts = []


        self.xpath_additions = {
            "names" :  "//td[2]",
            "districts": "//td[1]",
            "links": "//td[2]//a",
            "parties": "//td[3]",
            "states" :  "//caption"
        }

        self.datatype_lists = {
            "names" : [],
            "districts": [],
            "links": [],
            "parties": [],
            "states" : []
        }

        self.name_state = {}

    def __open(self) ->None:
        
        self.driver = self.driver.init_driver()

        self.driver.get('https://www.house.gov/representatives')

    def run(self) -> None:
        '''it makes sense right? no it does not'''

        data_search_order = [
            "names",
            "links",
            "parties",
            "districts",
        ]

        for state_num in range(1, 56+1):
            state_table_xpath = f'//*[@id="by-state"]/div/div//table[{state_num}]'

            state_name = self.driver.find_elements(By.XPATH, state_table_xpath + self.get_datatype_xpath("states"))

            self.get_datatype_list("states").append(state_name)

            for type_of_data in data_search_order:

                data_elem_list = self.driver.find_elements(By.XPATH, state_table_xpath + self.get_datatype_xpath(type_of_data))

                #sets the data string list as the appropiate class attribute of the data
                #e.g self.names = [name_elem.text for name_elem in name_elem_list]
                data_string_list = []

                if type_of_data == 'link':
                    data_string_list = [elem.get_attribute('href') for elem in data_elem_list]
                else:
                    data_string_list = [elem.text for elem in data_elem_list]

                    if type_of_data == 'name':

                        for name in data_string_list:
                            self.name_state[name] = state_name

                
                self.get_datatype_list(type_of_data).append(data_string_list)

        self.driver.quit()

    def get_datatype_list(self, datatype: str) -> list:
        '''returns the list the stores the specified datatype'''

        if datatype in self.datatype_lists:
            
            return self.datatype_lists[datatype]

        else:
            print("UNRECOGNIZED DATA TYPE TO SEARCH FOR")
            return


    def get_datatype_xpath(self, datatype: str) -> str:
        """returns the appropriate xpath"""

        if datatype in self.xpath_additions:
            
            return self.xpath_additions[datatype]

        else:
            print("UNRECOGNIZED DATA TYPE TO SEARCH FOR")
            return


    def get_mass_data(self) -> list:
        '''returns all the seperate data type lists as one list for the datatable.insert()'''
        data = []

        for index, name in enumerate(self.names):

            data.append([name, self.name_state[name], self.parties[index], self.districts[index], self.links[index]])

        return data

    def print_all_data(self):

        print(self.datatype_lists.items())

    

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
    