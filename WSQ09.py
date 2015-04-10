def factorial(n):
	x=n
	y=1
	while (x>1):
		y = y*x
		x = x-1
	return y

print("Vamos a calcular el factorial de un numero")
ans="y"
while(ans=="y"):
	n=int(input("Dame un numero positivo: "))
	f= factorial(n)
	if(n>1):
		print("El factorial de: ", n, " es ",f)
		ans=str(input("¿Quieres intentarlo de nuevo? "))
	else:
		print("Dame un numero positivo!!: ")
