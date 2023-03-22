#IMportation 
import csv 
import json
from projet import *
from ConvertCSV_to_JSON import *
from ConvertCSV_to_XML import *
from tabulate import tabulate
from datetime import datetime
class etudiant():
    def __init__(self,code,numero,nom,prenom,date_de_naissance,classe,note) :
        self.code=code
        self.numero=numero
        self.nom=nom
        self.prenom=prenom
        self.date_de_naissance=date_de_naissance
        self.classe=classe
        self.note=note
    def __str__(self) :
        return f"{self.code},{self.numero},{self.nom},{self.prenom},{self.date_de_naissance},{self.classe},{self.note}"
    
        
#MYCLASS
class transformerfichier():
    # CREATION CONSTRUCTEUR
    def __init__(self) :
        pass
    
    #VERIFICATION NUMERO
    def numvalide(numero):
        a=numero.isalnum()
        b=numero.isupper()
        c=any(i.isdigit() for i in numero)
        if a==True and b==True and c==True and len(numero)==7:
            return True
        else:
            return False
    
    #VERIFICATION PRENOM
    def verifprenom(prenom):
        j=0
        for i in prenom:
            if i.isalpha():
                j+=1
        if prenom[0].isalpha() and j>=3:
            return True
        else:
            return False
    #VERIFICATION NOM
    def verifnom(nom):
        j=0 
        for i in nom:
            if i.isalpha():
                j+=1
        if nom[0].isalpha() and j>=2:
            return True
        else:
            return False
        
    #VERIFICATION DATE 
    def verifdate(date):
        date=date.strip()
        for i in date: 
            if  not i.isalnum():
                date=date.replace(i,'/')          
        b=date.split('/')
        #CORRESPONDANCE DES MOIS EN CHIFFRE
        months={"jan":'1',"fev":'2',"mars":'3',"avr":'4',"mai":'5',"juin":'6',"juillet":'7',"Dec":'12'}
        for month in months.keys():
            if b[1].lower().startswith(month):
                b[1]=months[month]
                break

        for i in b[0] :
            if not i.isnumeric():
                return False
        for i in b[1] :
            if not i.isnumeric():
                return False
        for i in b[2] :
            if not i.isnumeric() :
                return False

        
        j=b[0]
        m=b[1]
        an=b[2]
        
        
        j=int(j)
        m=int(m)
        an=int(an)
        if 00<=an<=23:
            an=an+2000
        elif 25<=an<=99:
            an =an +1900
    
    
        try:
            d=datetime.datetime(an,m,j)
            e=d.strftime("%d/%m/%y")
            date=e
            return True
        except:
            return False
    #VALIDITE CLASSE
    def verifclasse(cl):
        a=True
        if cl !='':
            cl=cl.strip()
            if cl[0] in ['6','5','4','3'] and cl[len(cl)-1] in['A','B']:
                #print(cl[0],'em',cl[len(cl)-1])
                cl=cl[0]+"em"+cl[len(cl)-1]
            
        
            else:
                a=False
        return  a,cl

    
valide=[]
valide1=[]
invalide=[]
invalide1=[]
b=csv.reader(open ("Donnees_Projet_Python_DataC5.csv","r"),delimiter=",")
for i in b:
    etu=etudiant(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
    etu.classe=verifclasse(etu.classe)[1]
    if transformerfichier.numvalide(etu.numero)==True and transformerfichier.verifnom(etu.nom)==True and transformerfichier.verifprenom(etu.prenom)==True and transformerfichier.verifclasse(etu.classe)[0]==True :#and #transformerfichier.verifdate(etu.date_de_naissance)==True:
        valide1=[etu.code,etu.numero,etu.nom,etu.prenom,etu.date_de_naissance,etu.classe,etu.note]
        valide.append(valide1)
        valide1=[]
        #print(etu)
    else:
        invalide1=[etu.code,etu.numero,etu.nom,etu.prenom,etu.date_de_naissance,etu.classe,etu.note]
        invalide.append(invalide1)
        invalide1=[]

"""class validite():
    def __init__(self) :
        self.b=csv.reader(open ("Donnees_Projet_Python_DataC5.csv","r"),delimiter=",")
        
    #b=csv.reader(open ("Donnees_Projet_Python_DataC5.csv","r"),delimiter=",")

    for i in b:
        etu=etudiant(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
        etu.classe=verifclasse(etu.classe)[1]
        if transformerfichier.numvalide(etu.numero)==True and transformerfichier.verifnom(etu.nom)==True and transformerfichier.verifprenom(etu.prenom)==True and transformerfichier.verifclasse(etu.classe)[0]==True :#and #transformerfichier.verifdate(etu.date_de_naissance)==True:
            valide1=[etu.code,etu.numero,etu.nom,etu.prenom,etu.date_de_naissance,etu.classe,etu.note]
            valide.append(valide1)
            valide1=[]
            #print(etu)
        else:
            invalide1=[etu.code,etu.numero,etu.nom,etu.prenom,etu.date_de_naissance,etu.classe,etu.note]
            invalide.append(invalide1)
            invalide1=[]"""

print(tabulate(valide,headers=['CODE','Numero','Nom','Prénom','Date de naissance','Classe','Note']))
print(len(valide))
print("********************************************************************************************")
print(tabulate(invalide,headers=['CODE','Numero','Nom','Prénom','Date de naissance','Classe','Note']))
print(len(invalide))


    
    
    #if transformerfichier.numvalide(i[0]):
        #v.append(etu)
  