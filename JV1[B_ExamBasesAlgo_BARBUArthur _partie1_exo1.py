import random
myTable = [35,14,15,8,92] #Mon tableau et mes valeurs

i= myTable.pop(4) #Ici je stock la valeur placée en 4ème position dans une variable "i" et je la retire de mon tableau
e= myTable.pop(2) #Je fais de même avec la valeur placée en 2ème position en créant une variable "e"

myTable.insert(2,i) #Ici je récupère la valeur de ma variable "i" que j'insère en 2ème position
myTable.insert(4,e) #Même principe avec la variable "e" que j'insère en 4ème position

print (e)
print (i)
print (myTable) #Je print mon tableau et remarque que j'a ibien intervertie deux valeurs.