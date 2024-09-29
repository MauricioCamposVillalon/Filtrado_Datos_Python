nombres = ['Harry Houdini', 'Newton', 'David Blaine',
           'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']


magos=[]
cientificos=[]
otros=[]


for i in nombres:
    if (i=="Harry Houdini") | (i == "David Blaine") | (i== "Teller"):
        magos.append(i)
    elif (i=="Newton") | (i == "Hawking") | (i== "Einstein"):
        cientificos.append(i)
    else:
        otros.append(i)


def hacer_grandioso():
    """Añade la frase El gran  antes del nombre de cada mago"""
    for j in magos:
        x=magos.index(j)
        magos[x]="El gran "+j
    
        
        
def imprimir_nombres():
    lista=nombres.copy()
    
    print ("\n   Las Personas Ingresadas en la Lista son:")
    print ("   **************************************** ")
    for i in lista: 
        if (i=="Harry Houdini") | (i == "David Blaine") | (i== "Teller"):
            n=lista.index(i)
            lista[n]="El gran "+i
        else:
            n=lista.index(i)
            lista[n]= i
    for nomb in lista:
        pos=lista.index(nomb)
        print(f'  ({pos+1}) {nomb}')
        

 
def orden(posicion):
    for k in posicion:
        post=posicion.index(k)
        print(f'   {post+1}). {k}')  
         


hacer_grandioso()
imprimir_nombres()

print('\n____________________________________________')
print("   Lista completa antes de ser Modificado:\n")
orden(nombres)
print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
print("Nombre de los Magos Grandiosos")
orden(magos)
print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
print("Nombre de los Cientificos:")
orden(cientificos)
print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
print("Nombre de los Otros:")
orden(otros)

