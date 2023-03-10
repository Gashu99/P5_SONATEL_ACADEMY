library(stringr)

# FONCTION VERIFICATION NUMERO 
Verifnume=function(num){
  if (grepl("^[A-Z0-9]+$",num) & nchar(num)==7 & (grepl("\\d",num))){
    return(TRUE)
  }
  else{
    return( FALSE)
  }
  
}
b=read.csv("Donnees_Projet_Python_DataC5.csv",header=TRUE)


#SUPPRESSION DE LA COLONNE CODE
donnee=b[,2:7]
d=donnee[sapply(donnee$Numero, Verifnume),1]
d
