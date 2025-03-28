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
    #player = Trainer()
    #AI = TrainerAI()
    print("Selects 3 Pokemons of the list")
    for poke in Pokemons:
        print(f"{poke} \n")
    
    for i in range(3):
        selection = int(input(f"{i+1} Pokemon: "))
        Single_Pokemon = choosePokemon(Pokemons, selection)
        pokemons_player.append(Single_Pokemon)
    
    #player.team = pokemons_player
    #print("Player Team")
    #for poke in player.team:
     #   print(f"{poke}\n")

    
    #Selection for Pokemons for Ai
    for i in range(3):
        selectIA = random.randrange(1,80)
        SinlePokemon = choosePokemon(AIPlayer, selectIA)
        pokemons_AI.append(SinlePokemon)
    
    #AI.team = pokemons_AI
    #print("AI team")    
    #for poke in AI.team:
    #    print(f"{poke}\n")
   
   
    print("\n\n\nPokemons that you Selected")
    for poke in pokemons_player:
        print(f"{poke}\n")
    
     
    print("\n\n\nThese is the first Pokemon of the AI")    
    #for pokeIA in pokemons_AI:
    #   print(f"{pokeIA}\n")
    selectIAfirst = random.choice(pokemons_AI)
    print(selectIAfirst.NamePokemon)
    
    
    pokemon_to_use = int(input("Select First pokemon"))
    print(f"{pokemons_player[pokemon_to_use]}")
    
    #First Fight
    fightPokemons(selectIAfirst, pokemons_player,pokemon_to_use)
    AIPlayer.remove(selectIAfirst)
    print(f"This pokemon has fainted {selectIAfirst.NamePokemon}")
    
    """
    
    print("\n\n\nThese is the second Pokemon of the AI")
    selectIASecond = random.choice(pokemons_AI)
    print(selectIASecond.NamePokemon)
    
    #Second Fight
    fightPokemons(selectIASecond, pokemons_player,pokemon_to_use)
    AIPlayer.remove(selectIASecond)
    print(f"This pokemon has fainted {selectIASecond.NamePokemon}")
    
    
    #Third Fight
    print("\n\n\nThese is the Third Pokemon of the AI")
    selectIAThird = random.choice(pokemons_AI)
    print(selectIAThird.NamePokemon)
    
    
    fightPokemons(selectIAThird, pokemons_player,pokemon_to_use)
    print(f"This pokemon has fainted {selectIAThird.NamePokemon}")
    
    print("PLAYERS WINS")
    
"""   
    
    

def choosePokemon(List_Pokemons,number):
    for pokemon in List_Pokemons:
        if number == pokemon.NumPokedex:
            return pokemon


def actions():
    #The four attacks that it has
    ...
def fightPokemons(selectIAfirst, pokemons_player,pokemon_to_use):
    
    #Create iF and While, if the IA is more Rapid or not
    while(selectIAfirst.Hp > 0):
        print(pokemons_player[pokemon_to_use].attacks())
        choice = input("Attacks chose:")
        if choice in pokemons_player[pokemon_to_use].attacks():
            pokemon_attack = pokemons_player[pokemon_to_use].attacks()
            for attack, damage in pokemon_attack.items():
                if choice in attack:
                    damage_from = selectIAfirst.get_damage(pokemons_player[pokemon_to_use])
                    hp = (damage * damage_from)
                    selectIAfirst._Hp -= hp
                    print(selectIAfirst.Hp)


if __name__ == "__main__":
    main()