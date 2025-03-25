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
    
    
    def get_loseGame(self):
        faint_cnt = 0
        
        for poke in self.team:
            if poke.fainted:
                faint_cnt += 1
                
            if faint_cnt == 3:
                return True
            else:
                return False
    
    def is_turn(self):
        return self.token
    
    
        

#This makes Dad Trainer, all atributes came down
class TrainerAI(Trainer):
    def __init__(self):
        self.isIA = True
        
        #def verify_is_fainted(self):
            


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