edad = int(input("ingrese su edad: ")) #35
nombre = str(input("ingrese nombre:")) #a
if edad < 18:
	print("Eres menor de edad.")
elif 18 <= edad <= 40 and (nombre != "benito" or nombre != "joaquin") :
	print("Eres adulto joven y nadie te conoce")
#elif 18 <= edad <= 40:
	#print("Eres adulto joven ")
elif 41 <= edad < 65:
	print("Eres adulto.")
else:
	print("Eres un adulto mayor.")