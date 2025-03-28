import sys
import os
import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Pokemon.PokemonsCreator import pokemons

def main():
    AIPlayer = pokemons()[0]
    Pokemons = pokemons()[1]
    pokemons_player = []
    pokemons_AI = []

    print("Selects 3 Pokemons of the list")
    for poke in Pokemons:
        print(f"{poke} \n")
    
    for i in range(3):
        selection = int(input(f"{i+1} Pokemon: "))
        Single_Pokemon = choosePokemon(Pokemons, selection)
        pokemons_player.append(Single_Pokemon)

    
    #Selection for Pokemons for Ai
    for i in range(3):
        selectIA = random.randrange(1,80)
        SinlePokemon = choosePokemon(AIPlayer, selectIA)
        pokemons_AI.append(SinlePokemon)
    
   
    print("\n\n\nPokemons that you Selected")
    for poke in pokemons_player:
        print(f"{poke}\n")
    
     
    print("\n\n\nThese is the first Pokemon of the AI")    
    selectIAfirst = random.choice(pokemons_AI)
    print(selectIAfirst.NamePokemon)
    
    
    pokemon_to_use = int(input("Select First pokemon"))
    print(f"{pokemons_player[pokemon_to_use]}")
    
    #First Fight
    fightPokemons(selectIAfirst, pokemons_player,pokemon_to_use)
    print(f"This pokemon has fainted {selectIAfirst.NamePokemon}")
    
    
    
    print("\n\n\nThese is the second Pokemon of the AI")
    selectIASecond = random.choice(pokemons_AI)
    print(selectIASecond.NamePokemon)
    
    #Second Fight
    fightPokemons(selectIASecond, pokemons_player,pokemon_to_use)
    print(f"This pokemon has fainted {selectIASecond.NamePokemon}")
    
    
    #Third Fight
    print("\n\n\nThese is the Third Pokemon of the AI")
    selectIAThird = random.choice(pokemons_AI)
    print(selectIAThird.NamePokemon)
    
    
    print("PLAYERS WINS")
    
 

def choosePokemon(List_Pokemons,number):
    for pokemon in List_Pokemons:
        if number == pokemon.NumPokedex:
            return pokemon

def fightPokemons(selectIAfirst, pokemons_player, pokemon_to_use):
    player_pokemon = pokemons_player[pokemon_to_use]  
    player_turn = player_pokemon.speed >= selectIAfirst.speed  
    
    while selectIAfirst.Hp > 0 and player_pokemon.Hp > 0:
        if player_turn:
            print("\nplayer turn\n")
            player_attacks = player_pokemon.attacks()  
            print("Available attacks:", list(player_attacks.keys()))
            choice = input("Choose an attack: ")

            if choice in player_attacks:
                damage = player_attacks[choice]
                damage_multiplier = selectIAfirst.get_damage(player_pokemon)
                selectIAfirst.Hp -= damage * damage_multiplier
                print(f"HP: {selectIAfirst.Hp} \n")
        else:
            print("\nAI turn for attacking\n")
            ia_attacks = selectIAfirst.attacks()
            if ia_attacks:
                choice, damage = random.choice(list(ia_attacks.items()))
                damage_multiplier = player_pokemon.get_damage(selectIAfirst)
                player_pokemon.Hp -= damage * damage_multiplier
                print(f" HP: {player_pokemon.Hp} \n")

        
        player_turn = not player_turn

    if selectIAfirst.Hp <= 0:
        print("You won!")
    else:
        print("You lost!")

if __name__ == "__main__":
    main()