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
from unidecode import unidecode

model = {}

count = 0
col= ['date','vues','type','vente par tranche','promesse de vente',"type location",
              'promotion','type bien','avancement','contact',"haut standing",'ville',                                             
              'quartier','residence','proximite','superficie','etage','pieces',                                      
              'plusieurs logements', 'exposition exterieur','caracteristiques interieur',
              'commodites','prix']

file1 = open("preproccess20.csv", "r") 
count = 0
dataframe =  pd.DataFrame() 
while True:
    count += 1
    
    # Get next line from file
    line = file1.readline()
    try:
        
        line = line.replace('none',"null")
    except :     
        pass
    #print (line)
    if not line:
        break 
 
    try: 
        model = json.loads(line)
        
        print('_______________')
        print (model['ville'], model['quartier'], model['prix'], model["vues"])#type; type bien avancement // 
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
        try : 
           model =  model.drop(columns=['proximité'])
        except : 
            pass
        try : 
           model =  model.drop(columns=['étage'])
        except : 
            pass
        try : 
           model =  model.drop(columns=['pièces'])
        except : 
            pass
        
        try : 
           model =  model.drop(columns=['commodités'])
        except : 
            pass
        try : 
            
            model.loc[0,'prix']= model.loc[0,'prix'].replace("da","")
            model.loc[0,'prix']= model.loc[0,'prix'].replace(" ","")
            model.loc[0,'prix']= model.loc[0,'prix'].replace(" ","")
            if not(model.loc[0,'prix'].isnumeric()):
                model.loc[0,'prix']=None 
         
                
        except : 
            pass
        try:         
            if (model.loc[0,'prix'].integer()<=10000):
                model.loc[0,'prix']=None
        except : 
            pass
        try:         
            if (model.loc[0,'prix'].integer()>=1000000000):
                model.loc[0,'prix']=None
        except : 
            pass
        
        #remove columns not in 
             
        #print (model)
        try : 
             for  c in model.columns :
                if (c not in col ): 
                   model=  model.drop([c], axis=1, inplace=True)
        except: 
            pass 
        dataframe = dataframe._append(model )
        
        print (count)
    
        
    except Exception as e :
        print (f"""error:{e}""")
    
     
print (dataframe.shape)



file1.close()
dataframe.to_csv('dataset20.csv')
