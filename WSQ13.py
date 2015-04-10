def bm(x):
	r= x
	o=r+(x/r)
	o=o/2
	return o
x=int(input("Dame un numero: "))
a=bm(x)
print("La raiz cuadrada del numero es:" +srt(a))
