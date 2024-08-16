class CoffeeMachine:

    def __init__(self):
        self._water_level = 10
        self._beans_quantity = 10

    @property
    def water_level(self):
        return self._water_level

    @water_level.setter
    def water_level(self, new_value):
        if isinstance(new_value, int):
            if new_value > 10:
                raise ValueError("The new value must be 10 or less!")
            else:
                self._water_level = new_value
        else:
            raise ValueError("The new value must be a number!")

    @property
    def beans_quantity(self):
        return self._beans_quantity
        
    @beans_quantity.setter
    def beans_quantity(self, new_value):
        if isinstance(new_value, int):
            if new_value > 10:
                raise ValueError("The new value must be 10 or less!")
            else:
                self._beans_quantity = new_value
        else:
            raise ValueError("The new value must be a number!")

    def _heat_water(self):
        print("Heating water")

    def _grind_beans(self):
        print("Grinding beans")
        print(f"Beans quantity: {self.beans_quantity}")

    def _pump_water(self):
        print("Pumping water")
        print(f"Water level: {self.water_level}")

    def make_coffee(self):
        if self.beans_quantity >=1:
            self.beans_quantity -=1
            self._grind_beans()
        else:
            raise ValueError("Running out of beans. Please refill!")
        if self.water_level >=1:
            self.water_level -=1
            self._heat_water()
            self._pump_water()
        else:
            raise ValueError("Running low on water. Please refill!")
        print("Coffee is ready!")

class FancyCoffeeMachine(CoffeeMachine):

    def __init__(self):
        super().__init__()
        self._milk_level = 10

    def froth_milk(self):
        print("Milk frothed")


class GroundCoffeeMachine(CoffeeMachine):
    def __init__(self):
        super().__init__()
        self._milk_level = 10
        
    def make_ground_coffee(self):
        print("Ground Coffee Made!")

#my_ground_machine = GroundCoffeeMachine()
#my_ground_machine.make_ground_coffee()

#my_fancy_machine = FancyCoffeeMachine()
#my_fancy_machine.make_coffee()

#my_coffee_machine = CoffeeMachine()
#print(f"Starting beans quantity: {my_coffee_machine.beans_quantity}")
#print(f"Starting water level: {my_coffee_machine.water_level}")
#my_coffee_machine.make_coffee()

class CoffeeMachine:
    
    def __init__(self, sugar):
        self.sugar = sugar
         
    def make_coffee(self):
        print(f"Making coffee with {self.sugar} sugars.")
        
class SugarDispenser(CoffeeMachine):
   
    def __init__(self, sugar):
        super().__init__(sugar)
        
#beverage = SugarDispenser(2)
#beverage.make_coffee()

class PodCoffeeMachine(CoffeeMachine):
    """
    A class describing a pod coffee maker

    Properties:
        No new properties

    Methods:

    """
    def __init__(self):
        """ Initialises the properties """
        super().__init__()
        """Added the beans quantity property to check if the pod value message works"""
        self._beans_quantity = 1

    def _pierce_pod(self):
        """ Pierces the foil pod """
        print("Pod successfully pierced")

    def _eject_waste(self):
        """ ejects the used pod """
        print("Pod ejected")

    def make_coffee(self):
        """inherits the make coffee method then becomes polymorphic by adding pod steps"""
        
        """water check is the same but the beans value error statement has changed so each if statement is present"""
        if self.water_level >= 1:
            self._heat_water()
        else:
            raise ValueError("Not enough water to make coffee!")
        if self.beans_quantity >= 1:
            self._pierce_pod()
        else:
            raise ValueError("No pod inserted to make coffee!")

        self._pump_water()
        self._eject_waste()
        print("Made a coffee-like drink!")        
        
#my_pod_coffee_machine = PodCoffeeMachine()
#my_pod_coffee_machine.make_coffee()

"""Want to make a prompting if statement, asking them which type of coffee machine they are using

If using regular machine, use regular machine function, 

if using ground coffee, use ground coffee machine function,

if using frothy machine, sugar, pod coffee, use those functions"""
