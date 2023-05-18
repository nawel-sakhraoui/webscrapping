# -*- coding: utf-8 -*-
# next step extract knowledge from data ? 
import openai
import json 
import time  
import re 
import functools
#en utilisant openAI mettre les données text dans des tableau clean 

openai.api_key  ="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"


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]



instruction=""" dans le dict final tout le mots en minuscule singulier, 
             mettre ce texte dans un dict avec les attributs suivants (Date, Vues,
            type: vente ou location, 
            vente par tranche ,
            promesse de vente,  
            type location : si location alors chercher le type  par mois ou 12mois ou 6mois  sinon none,
            promotion :si c'est une promotion vrai ou faux,
            type bien: villa ou  appartement ou local ou terrain ou autre type, 
            avancement: si vente logement fini ou carcasse ou plan ou en cours  1 seul mot,
            contact,
            haut standing :vrai ou faux ,
            ville,
            quartier,
            residence: afficher si different de  nom de contact sinon none,
            proximité: 2 mots ne pas citer la ville,ou le quartier, mettre en miniscule singulier,
            superficie :mettre dans une liste chiffre en m2 ne pas afficher l'unité,
            etage: sinon none,
            Pièces: sinon none,
            plusieurs logements :vrai ou faux, vrai si  length superficie>1,
            exposition exterieur :  2 mots ,
            caracteristiques interieur : 2 mots en metttre minuscule singulier sans s a la fin ,
            commodités :  liste  de 2mots resumé max 4  remove 'Electricité', 'Gaz', 'Eau', mettre en minuscule singulier sans s a la fin,
            prix: le prix en DA ):  
        
            """
            
model = {}

count = 0

file1 = open("rawdataLast.csv", "r") 
count = 0
commodites =[]
 
while True:
    count += 1
    
    # Get next line from file last 124
    line = file1.readline()
    if not line:
            break 
    try : 
            model = json.loads(line)
     
            prompt =f"""{instruction} '{line}'   """

            print("---------------")
            print(count)
            #print(prompt)
            #print (model)
            response = get_completion(prompt)
            #output.append(response)
            new= json.loads(response)
        
            response= response.replace('\n','').replace('_', ' ').replace('é','e').replace('è','e').lower()
            response = re.sub(u"é", 'e', response) 
            response = re.sub(u"è", 'e', response)
            print (response)
            with open("preproccessLast00.csv", "a") as f:
                f.write(response+"\n")
        
        
            # if line is empty
            # end of file is reached
            time.sleep(30)
    except Exception as e  :
        
            print (f'''erreur en lecture {e}''')
            time.sleep(30)
                 
     

file1.close()

