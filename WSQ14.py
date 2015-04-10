def cal(pre):
	f=pre
	e=(1+1/f)**f
	return (e)
	
pre=int(input("Dame el numero de decimales que quieres: "))
print("Es estimado de e es: ",cal(pre))
