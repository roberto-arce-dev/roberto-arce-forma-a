contador = 1
mayor: int
cant_num = 0
while True:
    try:
        if (cant_num ==  0):
            cant_num = int(input("Cuantos numeros: "))
        num= float (input(f"Numero {contador}: "))
        if(contador == 1):
            mayor = num
        if(mayor < num):
            mayor = num
        if contador < cant_num:
            contador+=1
            
        else:
            break
        
    except ValueError: 
        print ("el tipo de dato ingresado no es correcto")
print(f"El numero mayor fue: {mayor}")