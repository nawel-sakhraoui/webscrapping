# -*- coding: utf-8 -*-
import time 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import plotly.express as px


#recuperer les adresse des annonces webscrapping 

options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

for i in range(1631,4041):  #1631
    
    try :    
    
        driver.implicitly_wait(30) # seconds 
        driver.get("https://www.ouedkniss.com/automobiles/"+str(i))
        print("attendre le chargement...")
        time.sleep(5);
        links = []

        all_iframes = driver.find_elements(By.TAG_NAME,"iframe")
        #print ( driver.find_elements(By.TAG_NAME,"iframe")) 
        
        if len(all_iframes) > 0:
            
            driver.execute_script('''
        
            var elems = document.getElementsByTagName("iframe");
            for(var i = 0, max = elems.length; i < max; i++)
             
                 elems[i].hidden=true;
             
                         ''' )
            print(' Ads: ' + str(len(all_iframes)))
        else:
            print('No ads found')

        
        
        '''parent = driver.current_window_handle

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
        
        x=5000'''
        #driver.implicitly_wait(10) # seconds 
        #for j in range(0,1): 

        #    #x=x+1000
           
        #    #driver.implicitly_wait(10)
        
       
        
        driver.execute_script(f"window.scrollTo(0,4200)")
        time.sleep(2); 
        
        
        element2 = driver.find_element(By.ID, 'search-header')

        element = driver.find_element(By.CLASS_NAME, 'w-100')
        
        driver.execute_script("arguments[0].scrollIntoView(true);", element2)
        time.sleep(2)
        
        driver.execute_script(f"window.scrollTo(0,3400)")
        time.sleep(2);
        
        # execute scrollIntoView script with our element as the argument:
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        
        driver.execute_script(f"window.scrollTo(0,2500)")
        time.sleep(2); 
        
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2) 
        
        driver.execute_script(f"window.scrollTo(0,1600)")
        time.sleep(2);
        
       
        
        
      
        page_source = driver.page_source
        
        
        
        
        soup = BeautifulSoup(page_source,features="html.parser")
        #ii=0
        #jj=0
        for d in soup.find_all('div', class_='col-sm-6 col-md-4 col-lg-3 col-12'): 
            #ii+=1
            
            
            for a in d.find_all('a', href=True):
                #jj+=1
                #print (a["href"])
                
                if 'vente' in a['href']  or 'location' in a['href']:
                    if 'https://www.ouedkniss.com' in a["href"]: 
                        links.append(a['href']) 
                    else : 
                        links.append("https://www.ouedkniss.com"+str(a['href']))  
    
    
        """print (ii)
        print (jj)"""
        print('_________')
        print (len(links))
        print(i)
        delimiter = '\n'
        stringlinks = delimiter.join(links)
        with open("linksauto.csv", "a") as f:
            f.write(stringlinks+"\n")

        
     
        
    except Exception as e: 
                print (f'''erreur en lecture {e}''') 
                
                time.sleep(5) 