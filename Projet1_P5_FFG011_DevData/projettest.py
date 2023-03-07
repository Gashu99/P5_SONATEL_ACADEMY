import csv
from fonctionDUprojet import *

print("---------------------------------------------------------------")
print("|**************************MENU*******************************|")
print("---------------------------------------------------------------")
print("|1:AFFICHAGE DES INFORMATIONS(VALIDES OU INVALIDE AU CHOIX)   |")
print("--------------------------------------------------------------|")
print("|2:AFFICHAGE PAR NUMERO                                       |")
print("--------------------------------------------------------------|")
print("|3:AFFICHAGE DES 5 PREMIERES LIGNES                           |")
print("--------------------------------------------------------------|")
print("|4::AJOUT D INFORMATION                                       |")
print("--------------------------------------------------------------|")
print("|5:PAGINATION PAR PAS DE 5                                    |")
print("--------------------------------------------------------------|")
print("|6:PAGINATION   AU CHOIX                                      |")
print("---------------------------------------------------------------")
print("|7:SORTIR                                                     |")
print("---------------------------------------------------------------")

choix=int(input("Basez vous sur le menu pour faire votre choix:"))
while choix in [1,2,3,4,5,6,7]:
    if choix==1:
        affichevalideouinvalide()
    if choix==2:
        num=input("donner le numero que vous rechercher")
        affichageparnum(num)
    if choix==4:
        ajoutelement()

    #if choix==5:
        #pagination()
    if choix==7:
        exit()
    print("---------------------------------------------------------------")
    print("|**************************MENU*******************************|")
    print("---------------------------------------------------------------")
    print("|1:AFFICHAGE DES INFORMATIONS(VALIDES OU INVALIDE AU CHOIX)   |")
    print("--------------------------------------------------------------|")
    print("|2:AFFICHAGE PAR NUMERO                                       |")
    print("--------------------------------------------------------------|")
    print("|3:AFFICHAGE DES 5 PREMIERES LIGNES                           |")
    print("--------------------------------------------------------------|")
    print("|4::AJOUT D INFORMATION                                       |")
    print("--------------------------------------------------------------|")
    print("|5:PAGINATION PAR PAS DE 5                                    |")
    print("--------------------------------------------------------------|")
    print("|6:PAGINATION   AU CHOIX                                      |")
    print("---------------------------------------------------------------")
    print("|7:SORTIR                                                     |")
    print("---------------------------------------------------------------")

    choix=int(input("Basez vous sur le menu pour faire votre choix:"))

    
    