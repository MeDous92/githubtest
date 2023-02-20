# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 08:42:10 2021

@author: mohamed.elmougith
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 13:57:55 2021

@author: mohamed.elmougith
"""
'''This is to test github repos'''
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import csv
import os
import glob
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen



class Main():
    
    def __init__(self):
        global options
        currentp= os.getcwd()
        exceldir = currentp + '/ExcelFile'
        datap = currentp + '/chrome'
        options = Options()
        options.add_argument('user-data-dir={}'.format(datap))
        prefs = {'download.default_directory' : currentp}
        options.add_experimental_option('prefs', prefs)
        options = Options()
        prefs = {
          "translate_whitelists": {"ru":"it"},
          "translate":{"enabled":"true"}
        }
        options.add_experimental_option("prefs", prefs)
        # chromepath = os.getcwd() + r'\chrome\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        self.search_process()
        
    def search_process(self):
        self.driver.get('https://ru.kompass.com/searchCompanies?acClassif=&localizationCode=IT_03_015&localizationLabel=Milano&localizationType=district&text=&searchType=SUPPLIER')
        elems = self.driver.find_elements(By.CLASS_NAME, '//a[@href]')
        # print(elems)
        for elem in elems:
            print(elem.get_attribute("href"))

        
        # self.get_links()
        
    # def get_links(self):        
    #     pass
        
    # def create_dataframe(self):
    #     full_list= []
    #     columns= ['#', 
    #             'Linked Domains', 
    #             'Domain Rating', 
    #             'Ahrefs Rank',
    #             'Total Links Count',
    #             'Links for Domain (Percent %)',
    #             'Dofollow Links Count',
    #             'Dofollow Backlinks for Domain (Percent %)',
    #             'First Seen (desc)',
    #             'Referring domains',
    #             'Linked Domains',
    #             'Organic Traffic']
    #     df = pd.DataFrame()
    #     df.to_csv(os.getcwd() + r'/combinedcsv/allcsv.csv', index= False)
        
    #     downloadedp = os.getcwd() + r'/downloadedcsv'
    #     csv_files = glob.glob(os.path.join(downloadedp, "*.csv"))
    #     for f in csv_files:
    #         with open(f, 'r', encoding= 'utf8', newline= '') as csvfile:
    #             csvreader = csv.reader(csvfile)
    #             next(csvreader)
    #             for line in csvreader:
    #                 full_list.append(line)
    #     targetcsv = os.getcwd() + r'/combinedcsv/allcsv.csv'
    #     csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    #     with open(targetcsv, 'w', encoding= 'utf8', newline='') as f:
    #         writer = csv.writer(f, dialect='myDialect')
    #         writer.writerow(columns)
    #         for row in full_list:
    #             if (row[0] == ''):
    #                 continue
    #             writer.writerow((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))
                
    #     print('Congrats! Data downloaded and appended in one CSV file!')
    #     print('\n')
    #     print('==>> melmougith@gmail.com')
    #     textpath = os.getcwd() + '/combinedcsv'
    #     file = open("readme.txt", "w") 
    #     file.write("melmougith@gmail.com ====> Low price - High quality") 
    #     file.close() 
        
ArithmeticError
def main():
    window=Main()

    
if __name__=='__main__':
    main()
       
        
# test = AutoWeb()
# test.login_process()
# test.redirect_links_download()
# test.create_dataframe()

