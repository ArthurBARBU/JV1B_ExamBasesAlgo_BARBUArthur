indicePlusPetitElement=0 #J'attribue la valeur 0 par défaut à mas variable "indicePlusPetitElement"
myTable = [35,14,15,8,92] #Mon tableau


for g in range(0,len(myTable)): # Je créer une variable "g" qui agit dans sur les valeurs présentes dans mon tableau
    plusPetitElement = 100 # J'attribue la valeur 100 par défaut à mas variable "PlusPetitElement"
    for i in range(g,len(myTable)): # Je créer une variable "i" qui agit dans ma boucle "g"
        if(myTable[i] < plusPetitElement): # Première étape de ma boucle "i", si l'une des valeurs de mon tableau est inférieur à 100 alors...
            plusPetitElement = myTable[i] # Ma valeur "plusPetitElement" obtient la valeur qui était inférieur à 100
            indicePlusPetitElement = i # et ma variable "indicePlusPetitElement" obtient l'indice de la valeur inférieur à 100 puis la boucle recommence.


    print(plusPetitElement)
    stock=myTable[g] #Si "myTable[i] est supérieur à 100 je créer une variable "stock" qui garde ma plus petite valeur
    myTable[g]=myTable[indicePlusPetitElement] #la valeur de "g" est remplacé par l'indice de mon plus petit element
    myTable[indicePlusPetitElement]=stock # la variable "myTable[IndicePlusPetitElement]" reprend la valeur de "stock"



print(indicePlusPetitElement)
print(myTable) # Je print mon tableau désormais dans l'odre croissant.