from Pokemon import ClassPokemon as Pokemon


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
            
    
    
        

#This makes Dad Trainer, all atributes came down
class TrainerAI(Trainer):
    def __init__(self):
        self.isIA = True
    def verify_is_fainted(self):
        if self.get_loseGame() == False:
            if self.in_battle_fainted == True:
                self.in_battle = False
                i = 0
                while True:
                    if self.team[i].fainted == True:
                        i += 1
                    else:
                        self.in_battle = self.team[i]
                        self.team[i].on_field = True
                        break
                        
                        
            


class RandomAI(TrainerAI):
    def __init__(self):
        #DAD super Class
        super(RandomAI, self).__init__()
        self.choices = [ ] #Number of choices of the Ai
        
        



class MinimaxAI(TrainerAI):
    ...


class MMAlphaBetaAI(MinimaxAI):
    ...
    


class ExpectiMaxAI(MinimaxAI):
    ...