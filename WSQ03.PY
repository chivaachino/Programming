from timeit import default_timer as timer
import os
import time

start = timer()
print ("\n")
print ("Hola, haremos algunas operaciones con dos numero")
print ("\n")
print ("\n")
num1 = input ("Introduce el primer numero:")
print ("\n")
num2 = input ("Introduce el segundo numero:")
sum = num1 + num2
res = num1 - num2
pro = num1 * num2
div = num1 // num2
resi = num1 % num2
os.system('clear')
print ("La suma es: " + str(sum))
print ("La resta es: " + str(res))
print ("El producto es: " + str(pro))
print ("La divicion es: " + str(div))
print ("El residuo es: " + str(resi))
stop = timer()
total = stop - start
print ("\n")
print("El tiempo total es de: " + str(total))
