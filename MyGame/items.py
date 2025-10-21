#items.py

class Drug: #parent class

    
    def __init__(self, start: int, end: int)-> None: #constructor for class drug
        self.__start: int = start
        self.__end: int = end
        
    def get_start(self)-> int: #accessor for start position
        return self.__start
    
    def get_end(self)-> int: #accessor for end position
        return self.__end
    
    def apply_effect(self, position: int)-> int:  #mutator for original position
        return position

    def __str__(self)-> str: #string method to make output user friendly
        return "Drug moves from %d to %d" %(self.__start, self.__end)
    
class Bacteria(Drug): #subclass of Drug that moves player backward if they land on its position


    def __init__(self, start: int, end: int, effect_strength: int) -> None: #subclass constructor
        super().__init__(start, end)
        self.__effect_strength: int = effect_strength  

    def get_effect_strength(self) -> int: #accessor for strength
        return self.__effect_strength
        
    def apply_effect(self, position: int)-> int: #moves player to the end position if lands to it
        if position == self.get_start():
            print("Oh no! There was a bacteria at position %d. Going back to position %d" %
                  (self.get_start(), self.get_end()))
            return self.get_end()
        return position
        
    def __str__(self)-> str: #returns user friendly outcome
        return (
    "Bacterial effect: Due to strength %d of bacteria, you moved from %d to %d position"
    % (self.get_effect_strength(), self.get_start(), self.get_end())
)

class WBC(Drug): #subclass of Drug that moves player forward if they land on its position


    def __init__(self, start: int, end: int, rarity: str) -> None:
        super().__init__(start, end)
        self.__rarity: str = rarity

    def get_rarity(self) -> str: #accessor for rarity
        return self.__rarity

    def apply_effect(self, position: int) -> int: #moves player forward to the end positiion
        if position == self.get_start():
            print("White Blood Cell boosts you from %d to %d!" %
                  (self.get_start(), self.get_end()))
            return self.get_end()
        return position

    def __str__(self) -> str: #returns user friendly outcome
        return (
    "White Blood Cell effect: Due to rarity %s of WBC, you moved from %d to %d position"
    % (self.get_rarity(), self.get_start(), self.get_end())
)


    

    
                  
        
    
        
