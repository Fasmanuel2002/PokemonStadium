import sys
import os
import random


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pokemon.PokemonsCreator import pokemons  # Import Pokémon creation function

def main():
    AIPlayer = pokemons()[0]
    Pokemons = pokemons()[1]
    pokemons_player = []
    pokemons_AI = []

    print("Select 3 Pokémon from the list:")
    for poke in Pokemons:
        print(f"{poke} \n")
    
    for i in range(3):
        while True:
            try:
                selection = int(input(f"Select Pokémon {i+1} (Enter Pokedex Number): "))
                Single_Pokemon = choosePokemon(Pokemons, selection)
                if Single_Pokemon:
                    pokemons_player.append(Single_Pokemon)
                    break
                else:
                    print("Invalid selection. Try again.")
            except ValueError:
                print("Please enter a valid number.")

    ai_pokemon_numbers = random.sample(range(1, 80), 3)
    for num in ai_pokemon_numbers:
        SinglePokemon = choosePokemon(AIPlayer, num)
        pokemons_AI.append(SinglePokemon)

    print("\nYour selected Pokémon:")
    for poke in pokemons_player:
        print(f"{poke}\n")

 
    print("\nAI has selected its Pokémon.\n")

    
    selectIAfirst, selectIASecond, selectIAThird = pokemons_AI

    
    while True:
        try:
            pokemon_to_use = int(input("Select your first Pokémon (0-2): "))
            if 0 <= pokemon_to_use < len(pokemons_player):
                break
            print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")

    
    for ai_pokemon in [selectIAfirst, selectIASecond, selectIAThird]:
        print(f"\n\n\nAI's next Pokémon: {ai_pokemon.NamePokemon}")

        
        if pokemons_player[pokemon_to_use].Hp <= 0:
            print("Your Pokémon fainted! Choose another one:")
            while True:
                try:
                    pokemon_to_use = int(input("Select your next Pokémon (0-2): "))
                    if 0 <= pokemon_to_use < len(pokemons_player) and pokemons_player[pokemon_to_use].Hp > 0:
                        break
                    print("Invalid choice or Pokémon has fainted. Try again.")
                except ValueError:
                    print("Please enter a valid number.")

        fightPokemons(ai_pokemon, pokemons_player, pokemon_to_use)
        print(f"{ai_pokemon.NamePokemon} has fainted!")

    print("\n🎉 Congratulations! You won the Pokémon battle! 🎉")

def choosePokemon(List_Pokemons, number):
    for pokemon in List_Pokemons:
        if number == pokemon.NumPokedex:
            return pokemon
    return None 

def fightPokemons(selectIA, pokemons_player, pokemon_to_use):
    player_pokemon = pokemons_player[pokemon_to_use]  
    player_turn = player_pokemon.speed >= selectIA.speed  

    while selectIA.Hp > 0 and player_pokemon.Hp > 0:
        if player_turn:
            print("\nYour turn!\n")
            player_attacks = player_pokemon.attacks()
            print("Available attacks:", list(player_attacks.keys()))
            choice = input("Choose an attack: ")

            if choice in player_attacks:
                damage = player_attacks[choice]
                damage_multiplier = selectIA.get_damage(player_pokemon)
                selectIA.Hp -= damage * damage_multiplier
                print(f"AI's {selectIA.NamePokemon} HP: {selectIA.Hp} \n")
        else:
            print("\nAI's turn!\n")
            ia_attacks = selectIA.attacks()
            if ia_attacks:
                choice, damage = random.choice(list(ia_attacks.items()))
                damage_multiplier = player_pokemon.get_damage(selectIA)
                player_pokemon.Hp -= damage * damage_multiplier
                print(f"Your {player_pokemon.NamePokemon} HP: {player_pokemon.Hp} \n")

        player_turn = not player_turn  # Switch turns

    if selectIA.Hp <= 0:
        print("You won this round!")
    else:
        print("You lost this round!")

if __name__ == "__main__":
    main()
