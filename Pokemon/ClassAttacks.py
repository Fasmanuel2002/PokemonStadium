class Attacks:
    def __init__(self, idAttack, NameAttack, typeAttack, powerAttack,accuracy, pp):
        self._idAttack = idAttack
        self._NameAttack = NameAttack
        self._typeAttack = typeAttack
        self._powerAttack = powerAttack
        self._accuracy = accuracy
        self._pp = pp
        
    @property
    def idAttack(self): #Getter
        return self._idAttack   
    
    @idAttack.setter
    def idAttack(self, newIdAttack):
        if isinstance(newIdAttack, int):
            self._idAttack = newIdAttack
        else:
            raise ValueError("Not Number")
    
    
    @property
    def NameAttack(self): #Getter
        return self._NameAttack   
    
    @NameAttack.setter
    def NameAttack(self, newNameAttack):
        if isinstance(newNameAttack, str):
            self._NameAttack = newNameAttack
        else:
            raise ValueError("Name must be a string")    
            
    
    @property
    def typeAttack(self): #Getter
        return self._typeAttack   
    
    @typeAttack.setter
    def typeAttack(self, newtypeAttack):
        if isinstance(newtypeAttack, int):
            self._typeAttack = newtypeAttack
        else:
            raise ValueError("Not Number")  
    
    @property
    def accuracy(self): #Getter
        return self._accuracy
    
    @accuracy.setter
    def accuracy(self, newAccuracy):
        if isinstance(newAccuracy, float):
            self._accuracy = newAccuracy
        else:
            raise ValueError("Not Number")
    
    
    @property
    def pp(self): #Getter
        return self._pp
    
    @pp.setter
    def pp(self, newPP):
        if isinstance(newPP, int):
            self._newPP = newPP
        else:
            raise ValueError("Not Number")
    
    
    @property
    def powerAttack(self): #Getter
        return self._powerAttack
    
    @powerAttack.setter
    def powerAttack(self, powerAttack):
        if isinstance(powerAttack, int):
            self._powerAttack = powerAttack
        else:
            raise ValueError("Not Number")
            
        

    def __str__(self):
        return f"this Attack id{self._idAttack} \n has this name {self._NameAttack} \n is this type: {self._typeAttack} and this damage {self._damageAttack}"
