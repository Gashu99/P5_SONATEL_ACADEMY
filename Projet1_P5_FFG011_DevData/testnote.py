import re

def verifnote(list):
    isvalide=True
    #list=[ 'FTR3456G', 'Drame', 'Rama', '12/03/92', '5 eme B', 'SVT[12;20:19] #PC[13;14:10] #Francais[14;18:19] #SVT[16;19:14] #Anglais[14;15:18] #HG[10;07:20] #Math[19;17:18]']
    note=list[6]
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
        
    return tab1,a
list=[ 'AAD003','FTR3456G', 'Drame', 'Rama', '12/03/92', '5 eme B', 'SVT[12;20:19] #PC[13;14:10] #Francais[14;18:19] #SVT[16;19:14] #Anglais[14;15:18] #HG[10;07:20] #Math[19;17:18]']
list=verifnote(list)[0]
print(list)