my_string <- "Hello World"
for (i in 1:nchar(my_string)) {
  char <- substr(my_string, i, i)
  print(char)
}

decoupagechaine=function(chaine){
  for (i in 1:nchar(chaine)) {
    char <- substr(chaine, i, i)
    vect=c(char)
    #print(char)
    
  }
  return(vect)
}
j=0
chaine='Gassama'
a=strsplit(chaine,split="")
print(a[[1]][3])
for (i in a[[1]]){
  print(i)
}
k=0
a=strsplit(chaine,split="")
for (i in  1:nchar(chaine)){
  if (grepl("[[:alpha:]]",a[[1]][i])) {
    k=k+1
    
  }
}
if ((k>=2) & (grepl("[[:alpha:]]",substring(chaine,1,1)))){
  print("MERCI")
  
}

#VERIFIER S IL YA AU MOINS DEUX LETTRES 
check_two_letters <- function(str) {
  n_letters <- sum(grepl("[[:alpha:]]", str))  # Compter le nombre de lettres dans la chaîne
  return(n_letters >= 2)  # Renvoyer TRUE si la chaîne contient au moins deux lettres, et FALSE sinon
}

