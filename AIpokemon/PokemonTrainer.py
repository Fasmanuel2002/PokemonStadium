from Pokemon.ClassPokemon import Pokemon
from PokemonStadium.main import fightPokemons
import copy

#Set of actions
class Actions:
    def __init__(self, action, user, target = None):
        self.action = action
        self.user = user
        self.target = target
    

class Trainer:
    def __init__(self):
        self.team = [None, None, None]
        self.token = None #what is turn
        self.isIA = False
    
    
        self._in_battle = self.team[0]
        self.team[0].on_field = True
        self.in_battle_fainted = False
   
   
    
    def get_loseGame(self):
        faint_cnt = 0
        
        for poke in self.team:
            if poke.fainted:
                faint_cnt += 1
            return True if (faint_cnt == 3) else False
            
    
    def is_turn(self):
        return self.token
    
    def set_turn(self, _token):
            self.token = _token
            
@staticmethod
def simulate_action(state, action):
    new_state = copy.deepcopy(state)
    
    # Assuming action.action holds the attack object with a 'damage' attribute.
    attack = action.action
    user = action.user
    target = action.target

    # Use the target's method to compute damage multiplier based on the user.
    damage_multiplier = target.get_damage(user)
    damage = attack.damage * damage_multiplier
    target._Hp -= damage

    # Update target's fainted status
    if target._Hp <= 0:
        target.fainted = True
    
    return new_state

    
    
    #Pokemon.Pokemon.get_damage()
    
def minimax(state, depth, maximizingPlayer):
    v = float('-inf') 
           

