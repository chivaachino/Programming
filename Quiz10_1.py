def find_threes(lista): 
 n_lista=[]
 for num in lista:
  if (num%3 ==0 ):
   n_lista.append(num)
 return n_lista

lista=[]
ans="si"

print("Crearemos una lista.")
print("\n")

while ans=="y":
 num=int(input("Dame un valor: "))
 lista.append(num)
 cant=len(lista)
 print("Tienes ",cant," Valores en la lista")
 ans=input(str("Quieres agregar otro numero? (y/n): "))
 print("\n")

find_threes(lista)
lista_divisible=(find_threes(lista))
suma_divisibles=sum(find_threes(lista))

print("\n")
print("La lista, ",lista, "tiene ",cant," valores.")
print(lista_divisible," son divisibles entre 3")
print("el resultado de la suma de estos numeros es de ",suma_divisibles)
