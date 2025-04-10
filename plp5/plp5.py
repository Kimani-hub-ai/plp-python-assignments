# Base class
class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def show_identity(self):
        print(f"I am {self.name} from the {self.universe} universe.")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Inherited class
class Mutant(Superhero):
    def __init__(self, name, power, universe, mutation_type):
        super().__init__(name, power, universe)
        self.mutation_type = mutation_type

    def show_identity(self):
        print(f"I am {self.name}, a {self.mutation_type}-type mutant from {self.universe}.")

# Another subclass
class TechHero(Superhero):
    def __init__(self, name, power, universe, suit_name):
        super().__init__(name, power, universe)
        self.suit_name = suit_name

    def use_power(self):
        print(f"{self.name} activates {self.suit_name} and uses {self.power}!")
