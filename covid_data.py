#!/usr/bin/env python
# coding: utf-8

# In[25]:


# import packages
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import shutil
import glob
import os
from unicodedata import *
import time


# In[26]:


# open a chrome browser using selenium
driver = webdriver.Chrome(ChromeDriverManager().install())


# In[27]:


# go to web page where excel file links are located
driver.get("https://data.chhs.ca.gov/dataset/covid-19-time-series-metrics-by-county-and-state")


# In[28]:


# these options allow selenium to download files 
options = Options()
options.add_experimental_option("browser.download.folderList",2)
options.add_experimental_option("browser.download.manager.showWhenStarting", False)
options.add_experimental_option("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel")


# In[29]:


# initialize an object to the location on the web page and click on it to download
link = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/article/div/section[1]/ul/li[1]/div/a[2]')
link.click()

# Wait for 15 seconds to allow chrome to download file
time.sleep(15)


# In[30]:


# locating most recent .xlsx downloaded file 
list_of_files = glob.glob('/Users/ralph/Downloads/*.csv')
latest_file = max(list_of_files, key=os.path.getmtime)
print(list_of_files)


# In[31]:


# replace "\" with "/" so file path can be located by python
latest_file = latest_file.replace("\\", "/")
latest_file


# In[32]:


# we need to locate the old .csv file(s) in the dir we want to store the new csv file in
list_of_files = glob.glob('/Users/ralph/Documents/python_dashboard/california_covid_data_dashboard_project/*.csv')

# need to delete the old csv file(s) so if we download new csv file with same name we do not get an error while moving it
for file in list_of_files:
    print("deleting old csv file:", file)
    os.remove(file)

# Move the new file from the download dir to the github dir
shutil.move(latest_file, '/Users/ralph/Documents/python_dashboard/california_covid_data_dashboard_project/')

