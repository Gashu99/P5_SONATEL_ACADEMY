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
  k=0
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
  
}

#VERIFICATION PRENOM
verifprenom=function(prenom){
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

#VERIFICATION CLASSE
verifclasse=function(classe){
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
  
  datefinale=format(datefinale,"%d/%m/%y")
  print(datefinale)
  
  
}
date='  28/fev/23'
verifdate(date)
#VERIFICATION NOTE
verifnote=function(note){
  note=trimws(note)
  matiere=strsplit(note,split = '#')
  for (i in matiere){
    mt=strsplit(i,split = '\\[')
  }
  de=""
  for (i in mt){
    dev=strsplit(i,split = '\\|')
    
  }
  mt
  
  
}

