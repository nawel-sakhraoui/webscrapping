# -*- coding: utf-8 -*-
import pandas as pd 
import numpy as np 
from geopandas._vectorized import isna
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import math 
import plotly.express as px
#df=  df.drop(['Unnamed: 0'], axis=1, inplace=True)


df = pd.read_csv ('dataset20.csv' ,index_col=False)

print(df.shape)
#df= df.fillna(-1)
#print (df)



types =   [i for i in df['type'].unique() if i is not np.nan]
typesBien =  [i for i in df['type bien'].unique() if i is not np.nan] 

'''values=[]
#print (types)
for t in types: 
    p = df[df['type']==t].shape[0] * 100 / len(df)
    
    print (f'{t}:{round(p,2)}%')
    values.append(p)

df0 = pd.DataFrame({ 'type': types,
                    'percent': values,
})

fig = px.pie(df0, names='type', values='percent',title="type annonce")
fig.show()

print ("-------------"  )  
values = []
#print (typesBien)
for t in typesBien: 
    p = df[df['type bien']==t].shape[0] * 100 / len(df)
    values.append(p)
    
    print (f'{t}:{round(p,2)}%')
df0 = pd.DataFrame({ 'type': typesBien,
                    'percent': values,
})
df0= df0.sort_values(by=['percent'],ascending=False)
fig = px.bar(df0, x="type", y="percent", color="type", title="les types de biens")
fig.show()



agence =[]
for row in df['contact']: 
    print (row)
    if str(row)!="nan":
        agence.append("agence")
    else:
      
        agence.append("privé")    

    
df['agence']= agence

print ("-------------"  )  

p = df[df["contact"].isnull()].shape[0] * 100 / len(df)
    
print (f'vente via privé :{round(p,2)}%')    

#mediane de prix promotion vs privé 
subdf = df[(df['contact'].isnull()) &(df['type']=='vente') &(df['type bien']=='appartement')]
print(f"Total {subdf.shape}")
print(f'valeur Mediane privé  {subdf["prix"].median()}')


print ("-------------")
print (f'vente via agence :{round(100-p,2)}%')  
subdf = df[(df['contact'].notnull()) &(df['prix'].notnull())  ]
print(f"Total {subdf.columns}")
print(f' valeur Mediane Agence  {subdf["prix"].median()}')


fig = px.box(df[(df['prix']<10**8) &(df['prix'].notnull())& (df['type']=='vente') &(df['type bien']=='appartement')], y="prix", x="agence" ,title='vente appartement')
fig.show()

'''
print ("-------------"  )          
            

percent_missing = df.isnull().sum() * 100 / len(df)

print ('Pourcentage des valeurs NULL')

print (percent_missing.to_dict())

print( '--------------------*toute les villes--------------------------')
'''for t in types:
    for t1 in typesBien : 
     
        
       
        subdf = df[(df['type bien']==t1)&(df['type']==t)]

        if not(subdf.empty):
        
            print (subdf[["ville",'type','type bien', 'pieces','prix']].head(2))
            print(f"Total {subdf.shape}")
            
            print(f' valeur Mediane {subdf["prix"].median()}')
            print ("-------------")

fig = px.box(df[(df['prix']<10**8) &(df['prix'].notnull())& (df['type']=='location') ], y="prix", x="type bien" ,title='vente tpute les villes')
fig.show()
'''
percent_alger = df[df['ville']=="alger"].shape[0] * 100 / len(df)
percent_oran = df[df['ville']=="oran"].shape[0] * 100 / len(df)
percent_constantine= df[df['ville']=="boumerdes"].shape[0] * 100 / len(df)
percent_bejaia = df[df['ville']=="blida"].shape[0] * 100 / len(df)

percent_autre = 100-(percent_alger-percent_oran)


categorie =["oran","alger", 'boumerdes', 'blida', 'autre']
value = [percent_oran, percent_alger,percent_constantine, percent_bejaia,  percent_autre]


print(df.columns)
          
fig = px.pie( values=value,names=categorie)
fig.show()   




'''
   
print( '********Alger********')
percent_alger = df[df['ville']=="alger"].shape[0] * 100 / len(df)
print(f"{percent_alger}%")
for t in types:
    for t1 in typesBien : 
     
        
       
        subdf = df[(df['type bien']==t1)&(df['type']==t)& (df['ville']=="alger") ]

        if not(subdf.empty):
        
            print (subdf[["ville",'type','type bien', 'pieces','prix']].head(2))
            print(f"Total {subdf.shape}")
            print(f' valeur Mediane {subdf["prix"].median()}')
            print ("-------------")

print( '********Oran*******')
percent_oran = df[df['ville']=="oran"].shape[0] * 100 / len(df)
print(f"{percent_oran}%")

for t in types:
    for t1 in typesBien : 
     
        
       
        subdf = df[(df['type bien']==t1)&(df['type']==t)& (df['ville']=="oran") ]

        
        if not(subdf.empty):
            print (subdf[["ville",'type','type bien', 'pieces','prix']].head(4))
        
            print(f"Total {subdf.shape}")
            print(f' valeur Mediane {subdf["prix"].median()}')
            print ("-------------")
            
                
print( '************autres************')
percent_autre = 100-(percent_alger-percent_oran)
print(f"{percent_autre}%")

for t in types:
    for t1 in typesBien : 
     
        
       
        subdf = df[(df['type bien']==t1)&(df['type']==t)& (df['ville']!="alger") & (df['ville']!="oran")]

        
        if not(subdf.empty):
            
            print (subdf[["ville",'type','type bien', 'pieces','prix']].head(4))
        
            print(f"Total {subdf.shape}")
            print(f' valeur Mediane {subdf["prix"].median()}')
            print ("-------------")
    
        if t=="vente":
                fig = px.box(df[(df['prix']<10**8) &(df['prix'].notnull())& (df['type']==t) & (df['type bien']==t1) ], y="prix", x="categorie" ,title=f'{t}-{t1} ')
                fig.show()
        else :
                fig = px.box(df[(df['prix']<10**6) &(df['prix'].notnull())& (df['type']==t) & (df['type bien']==t1) ], y="prix", x="categorie" ,title=f'{t}-{t1} ')
                fig.show()'''
      

