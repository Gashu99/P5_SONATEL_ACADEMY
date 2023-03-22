import csv 
from projet import *

#notre fichier en csv
b=csv.reader(open ("Donnees_Projet_Python_DataC5.csv","r"),delimiter=",")
b1=[]
for i in b:
    b1.append(i)

#CONVERSION EN FICHIER XML
def convert_row(row):
    return """
    <etudiant>
        <CODE>%s</CODE>
        <Numero>%s</Numero>
        <Nom>%s</Nom>
        <Prenom>%s</Prenom>
        <Date_de_naissance>%s</Date_de_naissance>
        <Classe>%s</Classe>
        <Note>%s</Note>
    </etudiant>"""%(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
#print('/n'.join([convert_row(i) for i in b]))
#print(next(b))

def convert_rowjsonxml(row):
    return """
    <etudiant>
        <CODE>%s</CODE>
        <Numero>%s</Numero>
        <Nom>%s</Nom>
        <Prenom>%s</Prenom>
        <Date_de_naissance>%s</Date_de_naissance>
        <Classe>%s</Classe>
        <Note>%s</Note>
    </etudiant>"""%(row["CODE"],row["Numero"],row[ "Nom"],row["Pr\u00c3\u00a9nom"],row["Date de naissance"],row["Classe"],row["Note"])
    

with open('output.xml', 'w') as f:
    f.write("<?xml version='1.0' encoding='ISO-8859-1' standalone='no' ?>")
    f.write('\n')
    f.write("<ETUDIANTS>")
    f.write('\n'.join([convert_row(i) for i in b1[1:]]))
    f.write('\n')
    f.write("</ETUDIANTS>")


import xml.etree.ElementTree as ET
from lxml import etree

tree = etree.parse("output.xml")
for  Numero in tree.xpath("/ETUDIANTS/etudiant"):
    if numvalide(Numero.text) :
        print("hello")

