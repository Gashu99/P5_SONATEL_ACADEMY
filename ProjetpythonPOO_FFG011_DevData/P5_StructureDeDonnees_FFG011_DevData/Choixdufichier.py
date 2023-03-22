import csv 
import json
from projet import *
from ConvertCSV_to_JSON import *
from ConvertCSV_to_XML import *


c=input("veuillez choisir votre type de fichier d'entrée:")
v=[]
iv=[]
if c =='csv' or c=='CSV':
    b=csv.reader(open ("Donnees_Projet_Python_DataC5.csv","r"),delimiter=",")
    for i in b :
        if numvalide(i[1])==True and  verifnom(i[2])==True and verifprenom(i[3])==True and verifdate(i[4])==True and verifclasse(i[5])[0]==True: #and verifnote(i[6])[0]==True:
            v.append(i)
        else:
            iv.append(i)
    choix=input("dans queltype de fichier voules vous les données valides:")
    if choix=='json' or choix=='JSON':
        with open('DataValide.json','w') as fichierjson:
            a=json.dumps(v)
            fichierjson.write(a)
        
        with open('DataInvalide.xml', 'w') as f:
            f.write("<?xml version='1.0' encoding='ISO-8859-1' standalone='no' ?>")
            f.write('\n')
            f.write("<ETUDIANTS>")
            f.write('\n'.join([convert_row(i) for i in iv]))
            f.write('\n')
            f.write("</ETUDIANTS>")
    elif choix=='xml' or choix=='XML':
        with open('DataValidexml.xml', 'w') as f:
            f.write("<?xml version='1.0' encoding='ISO-8859-1' standalone='no' ?>")
            f.write('\n')
            f.write("<ETUDIANTS>")
            f.write('\n'.join([convert_row(i) for i in v]))
            f.write('\n')
            f.write("</ETUDIANTS>")
        
        with open('DataInValide.json','w') as fichierjson:
            a=json.dumps(iv)
            fichierjson.write(a)

elif c=='json' or c=='JSON':
    tab=[]
    with open('Data.json','w') as fichierjson:
        a=json.dumps(jsontab)
        fichierjson.write(a)
    val, inval=verificationjson()
    with open("DataValide.json",'r') as val:
        datavaljson=json.load(val)

    with open("DataInValide.json",'r') as inval:
        datainvaljson=json.load(inval)
    choix=input("dans quel type de fichier voulez vous les données valides")
    if choix=='xml' or choix=='':
        #On lui donne les données valides en xml la fonction convert_rowjsonxml se trouve au niveau du fichier ConvertCSV_to_XML.py
        with open('DataValidejsonxml.xml', 'w') as f:
            f.write("<?xml version='1.0' encoding='ISO-8859-1' standalone='no' ?>")
            f.write('\n')
            f.write("<ETUDIANTS>")
            f.write('\n'.join([convert_rowjsonxml(i) for i in datavaljson ]))
            f.write('\n')
            f.write("</ETUDIANTS>")
        #Les donnees invalides en csv 
        with open("DataInvalide.json",'r') as inval:
            datainvaljson=json.load(inval)
        with open('Donneesinvalidesjsontocsv.csv', 'w', newline='') as data_file:
            csv_writer = csv.writer(data_file)
 
            count = 0
            for data in datainvaljson:
                if count == 0:
                    header = data.keys()
                    csv_writer.writerow(header)
                    count += 1
                csv_writer.writerow(data.values())
            donnees=open('Donneesinvalidesjsontocsv.csv', 'r')
            for i in donnees:
                print(i)
 
            data_file.close()
    elif choix=='csv' or choix=='CSV':
        # ECRITURE DES DONNéE VALIDES EN CSV 
        with open("DataValide.json",'r') as val:
            datavaljson=json.load(val)
        with open('Donneesvalidesjsontocsv.csv', 'w', newline='') as data_file:
            csv_writer = csv.writer(data_file)
 
            count = 0
            for data in datavaljson:
                if count == 0:
                    header = data.keys()
                    csv_writer.writerow(header)
                    count += 1
                csv_writer.writerow(data.values())
            donnees=open('Donneesvalidesjsontocsv.csv', 'r')
            for i in donnees:
                print(i)
            data_file.close()

        with open('DataInValidejsonxml.xml', 'w') as f:
            f.write("<?xml version='1.0' encoding='ISO-8859-1' standalone='no' ?>")
            f.write('\n')
            f.write("<ETUDIANTS>")
            f.write('\n'.join([convert_rowjsonxml(i) for i in datainvaljson ]))
            f.write('\n')
            f.write("</ETUDIANTS>")
   
elif c=='XML' or c=='xml':
    print("")
            



    """print(fichierjson)
    print("les donnees valides en csv:")
    val,inval=affichevalideouinvalidecsv()
    val=open("Datavalidecsv.csv",'r')
    inval=open("DataInvalidecsv.csv",'r')
    for j in inval:
        tab.append(inval)
    print(tab)
    for i in val:
        print(i)
    print("les données invalides en xml:")
    with open('DataInvalidexml.xml', 'w') as fichierinvalide:
        fichierinvalide.write("<?xml version='1.0' encoding='ISO-8859-1' standalone='no' ?>")
        fichierinvalide.write('\n')
        fichierinvalide.write("<ETUDIANTS>")
        fichierinvalide.write('\n'.join([convert_row(i) for i in tab[1:]]))
        fichierinvalide.write('\n')
        fichierinvalide.write("</ETUDIANTS>")
    
    affichevalideouinvalide()
        with open('Datavalide.json','w') as fichier:
            a=json.dumps(v)
            fichier.write(a)"""
    
    
    
    
        
        

