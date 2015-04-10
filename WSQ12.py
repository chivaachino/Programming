def gcd(x,y):
    if (x==y):
        ans=x
    elif(x>y):
        ag=gcd((x-y),y)
    else:
        g=gcd(x,(y-x))
    return g


print("Maxico comun divisor :)")
a=int(input("Dame el primer numero: "))
b=int(input("Dame el segundo numbero: "))
res = gcd(a,b)
print("El maxico comun divisor de ", a, " y ", b, " es: ", res)

