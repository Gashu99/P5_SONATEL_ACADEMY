import csv
import json
from projet import *

#notre fichier en csv
jsontab=[]
b=csv.DictReader(open ("Donnees_Projet_Python_DataC5.csv","r"),delimiter=",")
for i in b:
    jsontab.append(i)

#CONVERSION EN FICHIER JSON
with open('Data.json','w') as fichierjson:
    a=json.dumps(jsontab)
    fichierjson.write(a)
def verificationjson():
    jsontab=[]
    b=csv.DictReader(open ("Donnees_Projet_Python_DataC5.csv","r"),delimiter=",")
    for i in b:
        jsontab.append(i)
    

    #CONVERSION EN FICHIER JSON
    with open('Data.json','w') as fichierjson:
        a=json.dumps(jsontab)
        fichierjson.write(a)
    
    v=[] 
    iv=[]
    for i in jsontab:
        if numvalide(i["Numero"])==True and  verifnom(i["Nom"])==True and verifprenom(i["Prenom"])==True and verifdate(i["Date de naissance"])==True :#and verifclasse(i[5])[0]==True: #and verifnote(i[6])[0]==True:
            v.append(i)
        else:
            iv.append(i)
    with open("DataValide.json","w") as f:
        fj=json.dumps(v)
        f.write(fj)

    with open("DataInValide.json","w") as finv:
        fjinv=json.dumps(iv)
        finv.write(fjinv)
    return f,fjinv
        
a,b=verificationjson()
print(a)


