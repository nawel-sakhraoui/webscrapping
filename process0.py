agence =[]
for row in df['contact']: 
    temp = str(row).lower()
    if "résidence" in temp or "residence" in temp or "house" in temp or  "agree" in temp or  "immo" in temp or 'agence' in temp or 'company' in temp or 'group' in temp or 'home' in temp or 'business' in temp or  'affaire' in temp  or 'promo' in temp  or 'consultant' in temp: 
        agence.append(True)
    else:
        print(temp)  
        agence.append(False)    

    
df['agence']= agence

print (chr(47))


contacts =  [i for i in df['contact'].unique() if i is not np.nan] 

print (f"contacts {len(contacts)}")
for c in contacts: 
    e = df[df['contact']==c].shape[0]
    print (f"{c}: {e}")
