# -*- coding: utf-8 -*-
import time 

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from exceptiongroup._catch import catch


import json
#recuperer les données brute des annonce 
options = webdriver.FirefoxOptions()

options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

listLinks =[]
with open("links20.csv", "r") as f:
       listLinks= f.readlines()

print(len(listLinks))
count =18017
for l in listLinks[count:] :#['https://www.ouedkniss.com/local-location-alger-dely-brahim-algerie-d34319891',"https://www.ouedkniss.com/appartement-vente-f5-alger-ouled-fayet-algerie-d34214774"]:
  
    try :
        
        print (f'''dict numero:{count}''')
        print(l)
        driver.implicitly_wait(30) # seconds 

        driver.get(l)
        time.sleep(3);
   
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

        
    
        keys=[""]
        #driver.switchTo().defaultContent();
        page_source = driver.page_source
        #print(page_source)
        soup = BeautifulSoup(page_source,features="html.parser")
        dict = {}
        
       
             
               
        for c in soup.find_all('div',class_='col-sm-9 col-7'):
            temp = c.next_element
            if "<" in str(temp) :
               
                if temp.span:
                    if 'mb-1' in temp.span['class'] :
                       
                        if  temp.find('span', class_="v-chip__content"):
                            temp2 = []
                            for  s in temp.find_all('span', class_="v-chip__content"):
                                temp2.append(s.next_element)
                        
                            keys.append(temp2)
                                
                         
 
                        else: 
                            keys.append(temp.span.next_element)
                            
                else : 
                       if temp.find("i", class_="v-icon"): 
                            if("red--text" in temp.i['class']): 
                                 keys.append(False)
                            if("green--text" in temp.i['class']): 
                                 keys.append(True)  
                             
                            
            else :
                keys.append(temp)
                
 
        keys = list(filter(lambda x: x != '', keys))
        i=0
        print (keys)
        
        for c in soup.find_all('div',class_='spec-name'):
          
            if (i <len(keys)):
                dict[c.next_element]= keys[i]
           
                i=i+1
            else :
                dict[c.next_element]= False
            
            
     
        try :
            dict['title']= soup.find("h1").next_element #.next_element 

        except : 
            pass
        try : 
            dict['description']= soup.find_all("meta", property="og:description")[0]["content"]
            dict["description"] = dict["description"].replace("\n", "")
          
        except : 
            pass
         
 
        try : 
            dict['price'] = soup.find_all("meta",property="product:price:amount")[0]["content"]
        except : 
            pass
    
        try : 
        
            dict['contact']= soup.find_all('h4', class_='text-h6 font-weight-medium text-capitalize')[0].next_element
    
        except: 
             pass
        
        print ('-------------------------')
          

        print (dict)

        count = count+1
            
        if dict :
            with open("rawdata30.csv", "a") as f:
                f.write(json.dumps(dict)+"\n")

        time.sleep(1)
        
    except  Exception as e :
                print (f"an error occured {e}") 
                time.sleep(2)
    
driver.close() 
                
     
   