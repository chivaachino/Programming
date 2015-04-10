import math

def total(list):
	x=0
	y=0
	while (x<10):
		y=y+(l[x])
		x=x+1
	return y

def promedio(list):
	x=t/10
	return x

def std(list):
	x=0
	y=0
	z=0
	while (x<10):
		y=((l[x])-a)**2
		x=x+1
		z=z+y
	w=math.sqrt(z/a)
	return w

list=[]
nums=0
print("Listas")
while(nums<10):
	n=float(input("Dame un nuemero: "))
	list.append(n)
	nums=nums+1
t=total(l)
a=promedio(l)
sd=std(l)
print("Total: ", t)
print("Promedio: ", a)
print("Desviacion estandar: ", sd)
