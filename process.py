# -*- coding: utf-8 -*-
import time 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


#recuperer les addresse des annonces webscrapping 

options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

for i in range(2,9353):  #range(9353, 1, -1):
    
    try :     
        driver.get("https://www.ouedkniss.com/immobilier/"+str(i))
        print("attendre le chargement...")
        time.sleep(3);
        
        links = []


        
        parent = driver.current_window_handle

        uselessWindows = driver.window_handles

 
        
        if(uselessWindows):
            try:
                uselessWindows.remove(parent)
                print(f"popup :{uselessWindows}")
                
                for  w in uselessWindows and w!=parent :
                    driver.switch_to.window(w)
                    
                    driver.close()
            except  Exception :
                print ("error in userless windows") 
            
        driver.switch_to.window(parent)
        
        page_source = driver.page_source
        soup = BeautifulSoup(page_source,features="html.parser")
        for a in soup.find_all('a', href=True):
            if 'vente' in a['href']  or 'location' in a['href']:
                if 'https://www.ouedkniss.com' in a["href"]: 
                    links.append(a['href']) 
                else : 
                    links.append("https://www.ouedkniss.com"+str(a['href']))  
    
        print (len(links))
        print(i)
        delimiter = '\n'
        stringlinks = delimiter.join(links)
        with open("links.csv", "a") as f:
            f.write(stringlinks+"\n")

        
     
        
    except Exception as e: 
                print (f'''erreur en lecture {e}''') 
                
                time.sleep(5) 
    
        