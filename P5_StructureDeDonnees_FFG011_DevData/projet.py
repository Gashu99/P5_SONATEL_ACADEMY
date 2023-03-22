#IMPORTATION DES PACKAGES
import csv 
import datetime
import re    
from tabulate import tabulate


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
#VERIFICATION DE LA DATE DE NAISSANCE


def verifdate(date):
    #date='29-01-2023'
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
date='12;02-98'

#VERIFICATION DES nOTES
def verifnote():
    list=[ 'FTR3456G', 'Drame', 'Rama', '12/03/92', '5 eme B', 'SVT[12;20:19] #PC[13;14:10] #Francais[14;18:19] #SVT[16;19:14] #Anglais[14;15:18] #HG[10;07:20] #Math[19;17:18]']
    note=list[5]
    note=note.strip()
    matiere=note.split('#')
    
    tab=[]
    for i in matiere:
        a=re.sub('[[,,;]',':',i)
        #print(a)
        e=a.replace(']',':')
        d=e.split(':')
        #print(d)
        tab.append(d)
        tab1=[]
        for j in tab:
            tab1.append(j[0:4])
        if tab1[0]==[]:
            del tab1[0]
        a=len(tab1)   
        s=0
        m=0
        sm=0

        #if 0>i[j]>20 or 0>i[l-1]>20 :
                #return False
            
        
        for i in tab1:
            l=len(i)
            for j in [1,l-2]:
                i[j]=float(i[j])
                i[l-1]=float(i[l-1])
                s+=i[j]
                
            moydev=s/(l-2)
            s=0
            moy=round((moydev + 2*float(i[l-1]))/3,2)
            m+=1
            sm+=moy
            i.append(moy)
        note=tab1
        moyennegenerale=round(sm/m,2)
        tab1.append(moyennegenerale)
    print(tab1)
        
    return tab1   

#print(verifnote())
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

#cl='     6emmmme B'
#print(verifclasse(cl))
            
        
#AFFICHAGE DES VALIDES ET INAVLIDES

def affichevalideouinvalide():
    v=[]
    iv=[]
    s=[]
    t=[]
    
    b=csv.reader(open ("Donnees_Projet_Python_DataC5.csv","r"),delimiter=",")
    b1=next(b)
    #print(b1)
    
   
    for i in b :
        i[5]=verifclasse(i[5])[1]

        if numvalide(i[1])==True and  verifnom(i[2])==True and verifprenom(i[3])==True and verifdate(i[4])==True and verifclasse(i[5])[0]==True: #and verifnote(i[6])[0]==True:
            v.append(i)
            
            
        else:
            iv.append(i)
    
    c=int(input("tapez 1 pour afficher le tableau des valides ou 2 pour celui des invalides"))

    if c==1:
        print(tabulate(v,headers=['CODE','Numero','Nom','Prénom','Date de naissance','Classe','Note']))
        print(len(v))
    elif c==2:
        print(tabulate(iv,headers=['CODE','Numero','Nom','Prénom','Date de naissance','Classe','Note']))
        print(len(iv))
#print(affichevalideouinvalide())


#AFFICHAGE PAR NUMERO
def affichageparnum(num):
    t=['CODE','Numero','Nom','Prénom','Date' 'de naissance','Classe','Note']
    b=csv.reader(open ("Donnees_Projet_Python_DataC5.csv","r"),delimiter=",")
    for i in b:
        if i[1]==num:
           print("|CODE         |Nom            |PRENOM |DATE DE NAISSANCE   |CLASSE      | NOTE                |")
           for j in range(len(i)):
                print("| ", i[j], end=(12 - len(str(i[j]))) * ' ')


#PAGINATION PAR 5 LIGNES
"""def pagination():
    b=csv.reader(open ("Donnees_Projet_Python_DataC5.csv","r"),delimiter=",")
    for i in b:
        print(tabulate(i[0:4],headers=['CODE','Numero','Nom','Prénom','Date de naissance','Classe','Note']))"""
       

def affichevalideouinvalidecsv():
    v=[]
    iv=[]
    s=[]
    t=[]
    
    b=csv.reader(open ("Donnees_Projet_Python_DataC5.csv","r"),delimiter=",")
    #b1=next(b)
    #print(b1)
    
   
    for i in b :
        i[5]=verifclasse(i[5])[1]

        if numvalide(i[1])==True and  verifnom(i[2])==True and verifprenom(i[3])==True and verifdate(i[4])==True and verifclasse(i[5])[0]==True: #and verifnote(i[6])[0]==True:
            v.append(i)

            
            
        else:
            iv.append(i)
    header=['CODE','Numero','Nom','Prénom','Date de naissance','Classe','Note']
    with open("Datavalidecsv.csv",'w') as file: 
        mywritter=csv.writer(file,delimiter=',')
        mywritter.writerow(header)
        mywritter.writerows(v)

    with open("DataInvalidecsv.csv",'w') as fileinvalide: 
        mywritter=csv.writer(fileinvalide,delimiter=',')
        mywritter.writerows(iv)
        
    return file,fileinvalide
#affichevalideouinvalidecsv()