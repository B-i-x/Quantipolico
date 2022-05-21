import os
from directory_scaner.directory_crawler import rep
from unidecode import unidecode

from selenium import webdriver
from selenium.webdriver.common.by import By

house_directory = 'https://www.house.gov/representatives'
driver = webdriver.Chrome(executable_path=r"C:\Users\alexr\Documents\Projects\Mathematical Politics\chromedriver_win32\chromedriver.exe")

def reformat(s, stype):

    if stype == 'blank':
        r = [name for name in s if name != ""]
        return r

def states(num_states):

    state_xpath = r"/html/body/div[2]/div/div[2]/section/div/div[2]/div/div/div/section[1]/div/div/div[2]/table[{}]/caption"

    sub = len("caption")

    for n in range(1,num_states+1): #too long of a for loop i think

        xpath = state_xpath.format(n)

        state = driver.find_element(By.XPATH, xpath).text

        row_xpath = xpath[:-sub] + r"/tbody//tr"

        rows = driver.find_elements(By.XPATH, row_xpath)

        

        col_select = row_xpath + r"[{}]//td[{}]"
        article_xpath = col_select + r"/a"


        district_col = 1
        name_col = 2
        party_col = 3

        
        for n, row in enumerate(rows):
            
            name_elem = row.find_element(By.XPATH, article_xpath.format(n + 1, name_col))

            
            district_elem = row.find_element(By.XPATH, col_select.format(n + 1, district_col))
            party_elem = row.find_element(By.XPATH, col_select.format(n + 1, party_col))

            r = rep(name_elem.get_attribute('href'),name_elem.text,state,party_elem.text,district_elem.text)

            print(r.name)
            
    
    

def individual():

    xpath = r"/html/body/div[2]/div/div[2]/section/div/div[2]/div/div/div/section[1]/div/div/div[2]/table[{}]/tbody//td[2]/a"
    
def indv_getattributes():
    territory_title = driver.find_elements(By.XPATH, '//table[@class="table"]//child::caption')
    emt_list = []
    #adds the text in all table elements into a list
    for n in territory_title:
        emt_list.append(n.text)
    #gets rid of any empty strings in previouos list
    without_empty_strings = [string for string in emt_list if string != ""]

    indv_statename_list = []
    name_list = []
    link_list = []
    indv_party_list = []
    indv_id_list = []
    district_list = []
    state_id_number = 1
    indv_id_number = 0
    for territory_name in without_empty_strings:
        #print(state_id_number)
        if state_id_number == 1:
            #the first one is a little different
            district_pathstring = '//table[@class="table"]//child::td[@headers="view-text-1-table-column"]'
            party_pathstring = '//table[@class="table"]//child::td[@headers="view-text-5-table-column"]'
        else:
            party_pathstring = '//table[@class="table"]//child::td[@headers="view-text-5-table-column--{}"]'.format(state_id_number) 
            district_pathstring = '//table[@class="table"]//child::td[@headers="view-text-1-table-column--{}"]'.format(state_id_number) 

        party = driver.find_elements(By.XPATH, party_pathstring)
        for p_element in party:
            indv_party_list.append(p_element.text)

        districts = driver.find_elements(By.XPATH, district_pathstring)
        for d in districts:
            district_list.append(d.text)


        #print(pathstring)
        indv_tname = '"state-' + str(territory_name).replace(' ','-').lower() + '"'
        xpathstr = '//caption[@id={}]//parent::table[1]//a'.format(indv_tname)
        numr_and_link = driver.find_elements(By.XPATH, xpathstr)

        raw_name = []
        for r in numr_and_link:
            indv_id_list.append(indv_id_number)
            indv_statename_list.append(territory_name)
            raw_name.append(r.text) 
            link_list.append(r.get_attribute('href'))
            indv_id_number += 1
        #print(initiallist)
        
        #reformatting text from web element
        #print(raw_namelink)
        for n in raw_name:
            string_one = n.replace('(link is external)','').replace(' ','').replace('.','').replace('"','').replace('-','')
            i = string_one.index(',')
            c_name = string_one[i+1:] + ' ' + string_one[:i]
            c_name_edit = unidecode(c_name)
            name_list.append(c_name_edit)

        state_id_number = state_id_number + 1
    #print(indv_id_list)
    #print(gen_list)
    #print(indv_party_list)
    #print(indv_statename_list)
    #print(indv_stateid_list)
    #print(district_list)
    attribute_list = list(zip(name_list, link_list, indv_party_list, indv_statename_list, district_list))
    driver.minimize_window()
    return attribute_list

def main():
    attribute_list = indv_getattributes()
    return attribute_list

if __name__ == "__main__":
    driver.get(house_directory)
    states(56)
    
