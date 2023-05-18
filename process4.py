# -*- coding: utf-8 -*-
# next step extract knowledge from data ? 

import json 
import ast
import time  
import pandas as pd 
import numpy as np 
from pandas.io.formats.printing import PrettyDict
from sklearn.preprocessing import LabelEncoder
import functools
from xdg.Menu import Separator

model = {}

count = 0

file1 = open("preproccessLast00.csv", "r") 
count = 0
dataframe =  pd.DataFrame() 
while True:
    count += 1
    
    # Get next line from file
    line = file1.readline()
    if not line:
        break 
 
    try: 
        model = json.loads(line)
            
        print('_______________')
        print (model.keys())#type; type bien avancement // 
        #ville village quartier nom residence => zipcode
        #exposition exterieur comomdités caracteristiques
        model = pd.DataFrame([model], columns=model.keys())
        try : 
           model =  model.drop(columns=['title'])
        except : 
            pass
        try : 
           model =  model.drop(columns=['description'])
        except : 
            pass
        try : 
           model =  model.drop(columns=['promotion immobiliere'])
        except : 
            pass
        
        #print (model)
        dataframe = dataframe._append(model )
                
        
    
    
    
    except Exception as e :
        print (f"""error:{e}""")
    
     
#print (dataframe)



file1.close()
dataframe.to_csv('datasetlast10.csv')
