#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from bs4 import BeautifulSoup as Soup
from selenium.webdriver.common.keys import Keys
import time
import requests
import numpy as np


# In[2]:


options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
options.add_argument("disable-infobars")

driver = webdriver.Chrome(options = options)
driver.maximize_window()
url = 'https://www.facebook.com'
driver.get(url)


# In[3]:



username = # your account
password = # your passwordd

elem = driver.find_element_by_id("email")
elem.send_keys(username)
elem = driver.find_element_by_id("pass")
elem.send_keys(password)        

elem.send_keys(Keys.RETURN)
time.sleep(5)

url = # the url of page
driver.get(url)
time.sleep(5)


# In[4]:


keywords = ["梅竹", "免費"]
prev = []
while(1):
    current = []
    final = []
    remove_pos = []
    for i in range(0,2):  #網頁下拉
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        
    soup = Soup(driver.page_source, "html.parser")
    articles = soup.find_all('div', class_='ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a')  #抓貼文
    
    for i in range(0,3):
        current.append(articles[i].text)
    
    print ("current: \n", current)
    
    print("prev: \n", prev)
        
    for i in range(0,3):
        if current[i] not in prev:
            final.append(current[i])

    print ("final: \n", final)
    
    prev = current
    
    flag = 0

    if final:
        print("strating to compare.......")
        
        for i in final:
            for j in keywords:
                if j in i:
                    headers = {
                    "Authorization": "Bearer " + "3FmmROfkHGiz4kUdSVNWF3uyuj35gZaHriNnLntlXzv",
                    "Content-Type": "application/x-www-form-urlencoded"
                    }
                    params = {"message": "有 【"+ j + "】 案件了 快打開FB!!!!!! "}

                    r = requests.post("https://notify-api.line.me/api/notify",
                              headers=headers, params=params)
#                     print(r.status_code)  #200
                    
                    if r.status_code == 200:
                        print("Found !! ", j)
                        flag = 1
        if flag == 0:
            print("Not Found !!!!")
    else:
        print("final is empty")
                        
    print("\n\n")
    time.sleep(180)
    driver.refresh()

