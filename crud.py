import os
clear=os.system("cls")
import time
from main import *



class Pokemon():
    
    print(pokemon1_id)                
    print(pokemon1_name)
    print(pokemon1_abilities)
    print(pokemon1_type)
    get_pokemon_data1()
    def __init__(self,nombrePokemon,identificadorPokemon,puntosVidaPokemon,puntoAtaquePokemon,tipoPokemon,debilidad,fortaleza):
            self.nombre=nombrePokemon  
            self.id=identificadorPokemon  
            self.pSalud=puntosVidaPokemon  
            self.pAtaque=puntoAtaquePokemon
            self.tipo=tipoPokemon  
            self.debilidad=debilidad 
            self.fortaleza=fortaleza

    
def pokedex():
    clear
    pokemon1=Pokemon(pokemon1_name,1,100,1000,"fuego","trabajar","comer")
    print(pokemon1(pokemon1.nombre))
        
    input()
    
while (True):
    print("Seleccione una de las tareas a realizar:")
    print("1) Pokedex")
    print("2) Duelo Pokemon")
    print("0) Salir \n")
    
    pokeMenu=int(input())
    
    if(pokeMenu==1):
        pokedex()
        
    elif(pokeMenu==2):
        get_pokemon_data1()
        time.sleep(2)
        
    elif(pokeMenu==0):
        #Salir
        break