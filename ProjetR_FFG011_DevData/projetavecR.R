library(stringr)

#Verification numero
verifnum=function(num){
  if (grepl("^[A-Z0-9]+$",num) & nchar(num)==7 & grepl("\\d",num)){
    return(TRUE)
  }
  else{
    return(FALSE)
  }
}


#VERIFICATION Nom
verifnom=function(nom){
  if (nchar(nom)>1){ 
  k=0
  nom=trimws(nom)
  nom1=substring(nom,1,1)
  decopositionnom=strsplit(nom,split="")
  for (i in  1:nchar(nom)){
    if (grepl("[[:alpha:]]",decopositionnom[[1]][i])) {
      k=k+1
      
    }
  }
  if ((k>=2) & (grepl("[[:alpha:]]",nom1))){
    
    return(TRUE)
    
  }
  else{
    return(FALSE)
  }
  }else{
    return(FALSE)
  }
  
  
}
#VERIFICATION PRENOM
verifprenom=function(prenom){
  if (nchar(prenom)>1){  
  k=0
  prenom1=substring(prenom,1,1)
  decopositionprenom=strsplit(prenom,split="")
  for (i in  1:nchar(prenom)){
    if (grepl("[[:alpha:]]",decopositionprenom[[1]][i])) {
      k=k+1
      
    }
  }
  if ((k>=3) & (grepl("[[:alpha:]]",prenom1))){
    
    return(TRUE)
    
  }
  else{
    return(FALSE)
  }
  
}
 }
#VERIFICATION CLASSE
verifclasse=function(classe){
  if (nchar(classe)>1){  
  a=TRUE
  b=TRUE
  classe=gsub(" ","",classe)
  classedecom=strsplit(classe,split = "")
  taille=nchar(classe)
  as.numeric(taille)
  last=c('A','B')
  if ((classedecom[[1]][1] %in% (3:6)) & ((classedecom[[1]][taille] %in% c('A','B')))){
    return(TRUE)
    
  }
  else{
    return(FALSE)
  }
  }
}

#VERIFICATION DATE
verifdate=function(date){
  date=trimws(date)
  sep=c(".","|",";"," ","-")
  for(i in (1:nchar(date))){
    if(substring(date,i,i) %in% sep){
      date =gsub(substring(date,i,i),'/',date)
    }
  }
  
  
  date=gsub('fev','02',date)
  date=gsub('janvier','01',date)
  date=gsub('mars','03',date)
  date=gsub('Decembre','12',date)
  datefinale=as.Date(date,"%d/%m/%y")
  
  datefinale=format(datefinale,"%d/%m/%Y")
  print(datefinale)
  
  
}
date='  28/mars/23'
verifdate(date)
#VERIFICATION NOTE
verifnote=function(note){
  note=trimws(note)
  matiere=strsplit(note,split = '#')
  for (i in matiere){
  a=str_replace_all(i,c("\\["=":","\\|"=":",";"=":","]"=":"))
  print(a)
  }
  # for (i in matiere){
  #   print()
  #   #mt=strsplit(i,split = '\\[')
  # }
  # # de=""
  # for (i in mt){
  #   dev=strsplit(i,split = '\\|')
  #   
  # }
  # mt
  # 
  
}
note="Math[11|13:06] #Francais[08|17:12] #Anglais[13|13:12] #PC[09"
verifnote(note)
#IMPORTATION DE MES DONNEES
b=read.csv('Donnees_Projet_Python_DataC5.csv',header = TRUE)
View(b)
#SUPPRESSION DE LA COLONNE CODE
donnee=b[,2:7]
View(donnee)
d=donnee[sapply(donnee$Numero,verifnum),]
d=d[sapply(d$Nom,verifnom),]
d
nrow(d)
donnee$Date.de.naissance
for (i in 1:length(donnee$Nom)){
  print(verifnom(donnee$Nom[i]))
  
}
for (i in 1:length(donnee$PrÃ.nom)){
  print(verifprenom(donnee$PrÃ.nom[i]))
  
}
for (i in 1:length(donnee$Classe)){
  print(verifclasse(donnee$Classe[i]))
  
}
for (i in 1:length(donnee$Date.de.naissance)){
  print(verifdate(donnee$Date.de.naissance[i]))
  
}