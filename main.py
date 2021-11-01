#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from functions import * 
import requests
import os
import time
from functions import *
import random as rd

rand1=rd.randint(1,400)
varia1=str(rand1)
rand2=rd.randint(1,400)
varia2=str(rand2)

url1 ='https://pokeapi.co/api/v2/pokemon/'+varia1
url2 ='https://pokeapi.co/api/v2/pokemon/'+varia2

#Variables separadas de Pokemon 1

id1=[]
name1=[]
abilitie1=[]
type1=[]

#Variables separadas de Pokemon 2
id2=[]
name2=[]
abilitie2=[]
type2=[]
 
#pAtaque

randAtaque1=rd.randint(5,33)
randAtaque1=int(randAtaque1)
randAtaque2=rd.randint(5,33)
randAtaque2=int(randAtaque2)


entrenador1=[]
entrenador2=[]
coin1=0
coin2=0

select1=0
select2=0
loko1=[]
loko2=[]
dueloLista1=Pokemon(id1,name1,abilitie1,type1,randAtaque1,6,7)
dueloLista2=Pokemon(id2,name2,abilitie2,type2,randAtaque2,6,7)
nomentrenador1=datosDuelo(loko1,name1)
nomentrenador2=datosDuelo(loko2, name2)


#def get_pokemon_data1(url='https://pokeapi.co/api/v2/pokemon/'+varia):
def get_pokemon_data1(url):
    pokemon1_id=[]
    pokemon1_name=[]
    pokemon1_abilities=[]
    pokemon1_type=[]
    
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        
    #Obtener ID de pokemon
        getID = payload.get('id', [])
        pokemon1_id.append(getID)
            

    #Obtener nombre de pokemon
        results = payload.get('forms', [])
        if results:
            for pokemon in results:
                name = pokemon['name']
                pokemon1_name.append(name)
            #print(pokemon1_name)

            
                        
    #Obtener habilidad del pokemon
        results = payload.get('abilities', [])
        if results:
            for abilities_nest in results:
                skills = abilities_nest['ability']
                habilidades=skills.get('name')
                pokemon1_abilities.append(habilidades)    
             
            #print(pokemon1_abilities)

            
    #Obtener tipo del pokemon
        results = payload.get('types', [])
        #print(results)
        for type_nest1 in results:
            type_nest1_1 = type_nest1['type']
            type_pokemon=type_nest1_1.get('name')
            pokemon1_type.append(type_pokemon)  
            return pokemon1_id, pokemon1_name,pokemon1_abilities,pokemon1_type 
         

primerPokemon=[]
def crearRegistros1(pokemon1_name):
    if len(primerPokemon)==0:
        for i in pokemon1_name:
            primerPokemon.append(i)
            id1.append(i)
            name1.append(i)
            abilitie1.append(i)
            type1.append(i)
        for i in range(3):    
            id1.pop()
        for i in range(2):    
            name1.pop()
        abilitie1.pop()
        del name1[0]
        del abilitie1[0:2]
        del type1[0:3]

        print("Registro de Pokemon #1 agregado satisfactoriamente")
        time.sleep(2)
        #print(primerPokemon)
    else:
        print("No es posible sobreescribir datos de Pokemon #1")
        time.sleep(2)  
        #print("Lista primer pokemon: ",primerPokemon)

segundoPokemon=[] 
def crearRegistros2(pokemon1_name):
    
    """ No vean estas proximas lineas . NO EXISTEN """
    if len(segundoPokemon)==0:
        for i in pokemon1_name:
            segundoPokemon.append(i)
            id2.append(i)
            name2.append(i)
            abilitie2.append(i)
            type2.append(i)
        for i in range(3):    
            id2.pop()
        for i in range(2):    
            name2.pop()
        abilitie2.pop()
        del name2[0]
        del abilitie2[0:2]
        del type2[0:3]
        """ Listo ahora pueden seguir viendo """
        
        print("Registro de Pokemon #2 agregado satisfactoriamente")
        time.sleep(2)
        #print(segundoPokemon)
    else:

        print("No es posible sobreescribir datos de Pokemon #2")
        time.sleep(2)    

    
    #print("Lista segundo pokemon: ",segundoPokemon)

def crearRegistros():

    crearRegistros1(get_pokemon_data1(url1))
    #print("Lista primer pokemon: ")
    
    crearRegistros2(get_pokemon_data1(url2))
    #print("Lista segundo pokemon: ")
    os.system("cls")

def leerRegistros():
    if len(primerPokemon)== 0:
        print("Registros de Pokemones vacío. Ingrese datos primero.")
        time.sleep(3)
    else:
        for i in lista:
            i.mostrarInfoPokemon()           

        
lista=[
    Pokemon(id1, name1, abilitie1,type1,randAtaque1,5,50),
    Pokemon(id2, name2, abilitie2,type2,randAtaque2,10,100)
    ]



def menuDueloPokemon():
        os.system("cls")
        maestro1=input(f"Ingrese nombre de maestro Pokemon N°1:  ")
        os.system("cls")
        maestro2=input(f"Ingrese nombre de maestro Pokemon N°2:  ")
        nomentrenador1.loko1=maestro1
        nomentrenador2.loko2=maestro2

        os.system("cls")   
        print("Sorteo elección de Pokemon y comienzo de partida:\n")
           
        coinChoice=int(input("Maestro 1: Presiona 1 para lanzar moneda"))
        if coinChoice==1:
            coin1=rd.randint(1,100)
            print(f"Maestro 1: Tu número es el {coin1}")
        time.sleep(2)   
        os.system("cls")    
        coinChoice=int(input("Maestro 2: Presiona 1 para lanzar moneda"))
        if coinChoice==1:
            coin2=rd.randint(1,100)
            print(f"Maestro 2: Tu número es el {coin2}")
        time.sleep(2)
        os.system("cls")    
        if coin1 > coin2:
            
            #MAESTRO 1
            print("Maestro 1 ha ganado \nSeleccione Pokemon a utilizar: \n")
            coin1=999
            print(f"1) {str(name1[0][0])} // ({str(dueloLista1.tipo[0][0])})")
            print(f"2) {str(name2[0][0])} // ({str(dueloLista2.tipo[0][0])})")
            
            opcMenu=int(input())
                
            if (opcMenu==1):
                print(f"El entrenador N°1 {nomentrenador1.loko1} ha elegido el Pokemon : {str(dueloLista1.nombre[0][0])} del tipo {str(dueloLista1.tipo[0][0])}" )     
                
            elif (opcMenu==2):
                print(f"El entrenador N°1 {nomentrenador1.loko1} ha elegido el Pokemon : {str(dueloLista2.nombre[0][0])} del tipo {str(dueloLista2.tipo[0][0])}")
                          
                
        else:
            
            #MAESTRO 2
            os.system("cls")
            print("Maestro 2 ha ganado \nSeleccione Pokemon a utilizar: ")
            coin2=999
            print(f"1) {str(name1[0][0])} ({str(dueloLista1.tipo[0][0])})")
            print(f"2) {str(name2[0][0])} ({str(dueloLista2.tipo[0][0])})")
            
            
            opcMenu=int(input())    
            if (opcMenu==1):
                global select1
                print(f"El entrenador N°2 {nomentrenador2.loko2} ha elegido el Pokemon : {str(dueloLista1.nombre[0][0])} del tipo {str(dueloLista1.tipo[0][0])}")
                select1=1
                
            elif (opcMenu==2):
                global select2
                print(f"El entrenador N°2 {nomentrenador2.loko2} ha elegido el Pokemon : {str(dueloLista2.nombre[0][0])} del tipo {str(dueloLista2.tipo[0][0])}")
                select2=1
                
            
        cvarDueloCoach1=str(nomentrenador1.loko1)    #DatosDuelo.nombreEntrenador
        cvarDueloID1=str(dueloLista1.id[0][0])       #Pokemon.IdentificadorPokemon
        cvarDueloNombrePokemon1=str(dueloLista1.nombre[0][0]) #Pokemon.nombrePokemon
        cvarDueloHabilidad1=str(dueloLista1.abilities[0][0])  #Pokemon.abilities
        cvarDueloTipo1=str(dueloLista1.tipo[0][0])  #Pokemon.tipoPokemon
        cvarDueloAtaque1=str(dueloLista1.pAtaque)   #Pokemon.pAtaque
        cvarDueloDebilidad1=str(dueloLista1.debilidad) #Pokemon.de
        cvarDueloFortaleza1=str(dueloLista1.fortaleza)
        
        cvarDueloCoach2=str(nomentrenador2.loko2)   
        cvarDueloID2=str(dueloLista2.id[0][0])
        cvarDueloNombrePokemon2=str(dueloLista2.nombre[0][0])
        cvarDueloHabilidad2=str(dueloLista2.abilities[0][0])
        cvarDueloTipo2=str(dueloLista2.tipo[0][0])
        cvarDueloAtaque2=str(dueloLista2.pAtaque)
        cvarDueloDebilidad2=str(dueloLista2.debilidad)
        cvarDueloFortaleza2=str(dueloLista2.fortaleza)
        if coin1==999: #Si gana el entrenador 1
            begin=int(input("Presione la tecla 1 para comenzar el ataque"))
            if begin==1:
                if (opcMenu==1):
                    
                        while dueloLista1.health >=1 or dueloLista2.health >=1:
                            random1_1_1=int(rd.randint(5,33))
                            random1_1_2=int(rd.randint(5,33))
                            
                            input("MAESTRO 1: Presione una tecla para ATACAR")
                            if input:
                                print(f"{cvarDueloNombrePokemon1} ha atacado a {cvarDueloNombrePokemon2} con {cvarDueloHabilidad1} , causándole {random1_1_1} puntos de daño")
                                dueloLista2.health=dueloLista2.health-random1_1_1
                                
                            input("MAESTRO 2: Presione una tecla para ATACAR")
                            if input:
                                print(f"{cvarDueloNombrePokemon2} ha atacado a {cvarDueloNombrePokemon1} con {cvarDueloHabilidad2} , causándole {random1_1_2} puntos de daño")
                                dueloLista1.health=dueloLista1.health-random1_1_2
                                                                  
                            if dueloLista1.health <=0 or dueloLista2.health <=0:    
                                print(f"Se ha acabado {cvarDueloNombrePokemon1}: Health: {dueloLista1.health} ")
                                print(f"Se ha acabado {cvarDueloNombrePokemon2}: Health: {dueloLista2.health} ")
                                time.sleep(3)
                                break    
                        
                        
                else:
                        while dueloLista1.health >=1 or dueloLista2.health >=1:
                            random1_2_1=int(rd.randint(5,33))
                            random1_2_2=int(rd.randint(5,33))
                            
                            input("MAESTRO 1: Presione una tecla para ATACAR")
                            if input:
                                print(f"{cvarDueloNombrePokemon2} ha atacado a {cvarDueloNombrePokemon1} con {cvarDueloHabilidad2} , causándole {random1_2_1} puntos de daño")
                                dueloLista1.health=dueloLista1.health-random1_2_1
                                
                            input("MAESTRO 2: Presione una tecla para ATACAR")
                            if input:
                                print(f"{cvarDueloNombrePokemon1} ha atacado a {cvarDueloNombrePokemon2} con {cvarDueloHabilidad1} , causándole {random1_2_2} puntos de daño")
                                dueloLista2.health=dueloLista2.health-random1_2_2
                                                                  
                            if dueloLista1.health <=0 or dueloLista2.health <=0:    
                                print(f"Se ha acabado {cvarDueloNombrePokemon1}: Health: {dueloLista1.health} ")
                                print(f"Se ha acabado {cvarDueloNombrePokemon2}: Health: {dueloLista2.health} ")
                                time.sleep(3)
                                break    
                        
        elif coin2==999: #Si gana el entrenador 2
            begin=int(input("Presione la tecla 1 para comenzar el ataque"))

            if begin==1:
                if select1==1:
                    
                    while dueloLista1.health >=1 or dueloLista2.health >=1:
                        random2_1_1=int(rd.randint(5,33))
                        random2_1_2=int(rd.randint(5,33))
                        input("MAESTRO 2: Presione una tecla para ATACAR")
                        print("PRINT 2-1")
                        if input:
                            print(f"{cvarDueloNombrePokemon1} ha atacado a {cvarDueloNombrePokemon2} con {cvarDueloHabilidad1} , causándole {random2_1_1} puntos de daño")
                            dueloLista2.health=dueloLista2.health-random2_1_1
                            if dueloLista1.health <=0 or dueloLista2.health <=0:    
                                print(f"Se ha acabado {cvarDueloNombrePokemon1}: Health: {dueloLista1.health} ")
                                print(f"Se ha acabado {cvarDueloNombrePokemon2}: Health: {dueloLista2.health} ")
                                time.sleep(3)
                                break    
                                
                        input("MAESTRO 1: Presione una tecla para ATACAR")
                        if input:
                            print(f"{cvarDueloNombrePokemon2} ha atacado a {cvarDueloNombrePokemon1} con {cvarDueloHabilidad2} , causándole {random2_1_2} puntos de daño")
                            dueloLista1.health=dueloLista1.health-random2_1_2
                                                                  
                            if dueloLista1.health <=0 or dueloLista2.health <=0:    
                                print(f"Se ha acabado {cvarDueloNombrePokemon1}: Health: {dueloLista1.health} ")
                                print(f"Se ha acabado {cvarDueloNombrePokemon2}: Health: {dueloLista2.health} ")
                                time.sleep(3)
                                break    
                        
                        
                elif select2==1:
                    while dueloLista1.health >=1 or dueloLista2.health >=1:
                        random2_2_1=int(rd.randint(5,33))
                        random2_2_2=int(rd.randint(5,33))
                        input("MAESTRO 2: Presione una tecla para ATACAR")
                        print("PRINT2-2")
                        if input:
                            print(f"{cvarDueloNombrePokemon2} ha atacado a {cvarDueloNombrePokemon1} con {cvarDueloHabilidad2} , causándole {random2_2_1} puntos de daño")
                            dueloLista1.health=dueloLista1.health-random2_2_1
                            if dueloLista1.health <=0 or dueloLista2.health <=0:    
                                print(f"Se ha acabado {cvarDueloNombrePokemon1}: Health: {dueloLista1.health} ")
                                print(f"Se ha acabado {cvarDueloNombrePokemon2}: Health: {dueloLista2.health} ")
                                time.sleep(3)
                                break    
                                                      
                        input("MAESTRO 1: Presione una tecla para ATACAR")
                        if input:
                            print(f"{cvarDueloNombrePokemon1} ha atacado a {cvarDueloNombrePokemon2} con {cvarDueloHabilidad1} , causándole {random2_2_2} puntos de daño")
                            dueloLista2.health=dueloLista2.health-random2_2_2
                                                                  
                        if dueloLista1.health <=0 or dueloLista2.health <=0:    
                            print(f"Se ha acabado {cvarDueloNombrePokemon1}: Health: {dueloLista1.health} ")
                            print(f"Se ha acabado {cvarDueloNombrePokemon2}: Health: {dueloLista2.health} ")
                            time.sleep(3)
                            break    


os.system("cls")    
while (True):

    print("====MENU PRINCIPAL====")
    print("\nSeleccione una de las tareas a realizar:")
    print("1) Pokedex")
    print("2) Duelo Pokemon")
    print("0) Salir \n")
    

    
    pokeMenu=int(input())
    
    if(pokeMenu==1):
        os.system("cls")
        print("Seleccione una de las tareas a realizar:\n")
        print(" 1) Crear registros")
        print(" 2) Listar datos")
        print(" 3) Modificar registros")
        print(" 4) Eliminar datos")
        print(" 0) SALIR\n")
        
        opcMenu=input()
        
        if (opcMenu=="1"):
            os.system("cls")
            crearRegistros()

        elif (opcMenu=="2"):
            os.system("cls")
            leerRegistros()

                    
        elif (opcMenu=="3"):
            os.system("cls")
            #Modificar Datos
            for i in lista:
                i.mostrarInfoPokemon()
            modificarDatos=int(input("Ingrese ID de POKEDEX a actualizar"))
            indice=0
            for per in lista:
                if per.id[0][0]==modificarDatos:
                    per.nombre[0][0]=input("Favor de ingresar el nombre: ")
                    per.abilities[0][0]=input("Favor de ingresar abilities : ")
                    per.tipo[0][0]=input("Favor de ingresar tipo ")
                    per.tipo[0][0]=input("Favor de ingresar Punto Ataque ")
                    indice+=1  
            os.system("cls")
        elif (opcMenu=="4"):
            os.system("cls")
            leerRegistros()
            #Eliminar Datos    
            print("Eliminar Persona:")

            idELimina=int(input("Ingrese ID de POKEDEX a eliminar: "))

            indice=0
            for per in lista:
                if per.id[0][0]==idELimina:
                    lista.pop(indice)  
                    print(f"Los datos de {per.nombre[0][0]} han sido eliminados satisfactoriamente !!")
                indice+=1
                
            delList2=segundoPokemon.clear()
            time.sleep(3)
            os.system("cls")

        elif (opcMenu=="0"):
            #Salir
            pass
        else:
            pass
        
                   
      
    elif(pokeMenu==2):

        menuDueloPokemon()

        


    elif(pokeMenu==0):

        print("Maestro 1: ",dueloNombreMaestro1)
        print("Maestro 2: ",dueloNombreMaestro2)
        print("Pokemon 1",dueloNombrePokemon1)
        print("Pokemon 2:",dueloNombrePokemon2)
        print(len(dueloNombrePokemon1))
        print(len(dueloNombrePokemon2))
        


        

if __name__ == '__main__':
    get_pokemon_data1(url1)
    print(get_pokemon_data1(url1)) 
    get_pokemon_data1(url2)
    print(get_pokemon_data1(url2)) 
    

