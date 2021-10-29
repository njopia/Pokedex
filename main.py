#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
os.system("cls")


# Valores globales
puntosVida=100

pokemon1_id=[]
pokemon1_name=[]
pokemon1_abilities=[]
pokemon1_type=[]



                
def get_pokemon_data1(url='https://pokeapi.co/api/v2/pokemon/400'):
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
                
                
    print(pokemon1_id)                
    print(pokemon1_name)
    print(pokemon1_abilities)
    print(pokemon1_type)


def new_func(results):
    if results:
        for pokemon in results:
            name = pokemon['name']
            pokemon1_name.append(name)
        #print(pokemon1_name)
           
if __name__ == '__main__':
    url ='https://pokeapi.co/api/v2/pokemon/400'
    get_pokemon_data1()
    

