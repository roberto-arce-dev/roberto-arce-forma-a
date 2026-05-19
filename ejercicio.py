try:
    a= "Roberto Arce"
    b= ["R","o","b","e","r","t","o"," ","A","r","c","e"]
    c= []
    print(a[0])
    print(b[0])
    print ("for array ")
    for i in b:
        print(i, end="")
        
    print ("\n for string ")
    for i in a: 
        c.append(i)
        print(i, end="")

    print(f"\n{b==c}")
    print(b)
    print(c)
except SyntaxError:
    print("tienes un error de sintaxis")
10/0
