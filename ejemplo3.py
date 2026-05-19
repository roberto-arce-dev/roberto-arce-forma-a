import random

letras = list('ABCDEFGH')
random.shuffle(letras)

while letras:
   try:.
   
      entrada = int(input(f"ingresa un numero entre 0 {len(letras)-1}: "))
   except ValueError:
      print("debes ingresar una numero")

   if 0<= entrada < len(letras):
      print(f"Haz elegido la letra {letras[entrada]}")
      letra_eliminada= letras.pop(entrada)
