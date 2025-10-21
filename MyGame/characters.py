#characters.py

from items import Drug


class Character:
    
    def __init__(self, name: str) -> None: #constructor
        self.__name: str = name
        self.__inventory: List[Drug] = []
        self.__health: int = 5
        self.__position: int = 0

    def add_item(self, item: Drug) -> None: #method to add to inventory
        self.__inventory.append(item)

    def use_special_ability(self, other: 'Character') -> None: 
        print("%s uses a basic ability." % self.__name)

    def get_name(self) -> str: #accessor for name
        return self.__name

    def get_inventory(self) -> list[Drug]: #accessor for inventory
        return self.__inventory

    def get_health(self) -> int: #accessor for health
        return self.__health

    def get_position(self) -> int: #accessor for position
        return self.__position

    def set_health(self, new_health: int) -> None: #mutator for health
        self.__health = new_health

    def set_position(self, n_position)-> None:
        self.__position = n_position

    def __str__(self) -> str:
        hearts: str = "<>" * self.__health

        if self.__inventory:
            inventory_list: list[str] = [str(item) for item in self.__inventory]
            inventory_str: str = ", ".join(inventory_list)
        else:
            inventory_str = "Empty"

        return (
            "Name: %s\nHealth: %s (%d)\nInventory: %s"
            % (self.__name, hearts, self.__health, inventory_str)
        )


class Player(Character):


    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__special_ability_used: bool = False

    def use_special_ability(self, other: 'Character') -> None:
        if self.__special_ability_used:
            print("%s has already used their ability." % self.get_name())
            return

        current_health: int = self.get_health()
        if current_health < 5:
            self.set_health(current_health + 1)
            print("%s used their ability to heal 1 heart!" % self.get_name())
        else:
            print("%s is already at full health." % self.get_name())

        self.__special_ability_used = True

    def __str__(self) -> str:
        return super().__str__()
