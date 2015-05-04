def find_threes(lis): #funcion para crear la nueva lista con elementos divisibles entre 3
 n_lis=[]
 for num in lista:
  if (num%3 == 0 ):
   n_lis.append(num)
 return n_lis

lis=[] #nueva lista
ans="si"

print("Crearemos una lista.")
print("\n")

while ans=="si": #Elementos de la lista
 num=int(input(" Introduce un valor -> "))
 lis.append(num)
 cant=len(lis)
 print("tienes ",cant," Valores en la lista")
 ans=input(str("Quieres agregar otro numero? (si/no) -> "))
 print("\n")

 #llamado de funciones
find_threes(lis)
lista_divisible=(find_threes(lis))
suma_divisibles=sum(find_threes(lis))

#salidas
print("\n")
print("La lista, ",lis, "tiene ",cant," valores.")
print(lista_divisible," son divisibles entre 3")
print("el resultado de la suma de estos numeros es de ",suma_divisibles)
