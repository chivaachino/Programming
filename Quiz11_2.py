def check_banana(a):
 archivo=open("texto.txt",'r')
 cantidad=0
 for i in archivo:
  r=i.lower()
  sub=r.find('banana')
  while sub !=-1:
   cantidad=cantidad+1
   sub=r.find('banana',(sub+1))
 return(cantidad)
 close("texto.txt")

cant=check_banana('texto.txt')
print("la palabra banana aparece ",cant," veces en el archivo")
