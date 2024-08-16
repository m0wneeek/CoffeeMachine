class CoffeeMachine:
    """
    A class describing a coffee machine

    Properties:
        water_level: int, max value 10, level of water in the tank
        beans_quantity: int, max value 10, quantity of beans in the hopper

    Methods:
        make_coffee: makes a cup of coffee
    """
    def __init__(self):
        """ Initialises the properties """
        self._water_level = 10
        self._beans_quantity = 10

    @property
    def water_level(self):
        """ water_level getter """
        return self._water_level

    @water_level.setter
    def water_level(self, new_value):
        """
        water_level setter method

        Args:
            new_value: int specifying the quantity

        Returns:
            None

        Raises:
            ValueError: if the value is more than 10
            ValueError: if the value is not an int
        """
        if isinstance(new_value, int):
            if new_value > 10:
                raise ValueError("The new value must be 10 or less!")
            else:
                self._water_level = new_value
        else:
            raise ValueError("The new value must be a number!")

    @property
    def beans_quantity(self):
        """ beans_quantity getter """
        return self._beans_quantity

    @beans_quantity.setter
    def beans_quantity(self, new_value):
        """
        beans_quantity setter method

        Args:
            new_value: int specifying the quantity

        Returns:
            None

        Raises:
            ValueError: if the value is more than 10
            ValueError: if the value is not an int
        """
        if isinstance(new_value, int):
            if new_value > 10:
                raise ValueError("The new value must be 10 or less!")
            else:
                self._beans_quantity = new_value
        else:
            raise ValueError("The new value must be a number!")

    def _heat_water(self):
        """ Heats the water """
        print("Heating water")

    def _grind_beans(self):
        """ Grinds the beans """
        print("Grinding beans")

    def _pump_water(self):
        """ Pumps the hot water """
        print("Pumping water")

    def _eject_waste(self):
        """ Ejects the waste grounds """
        print("Ejecting waste")

    def make_coffee(self):
        """ Makes the coffee """
        if self.water_level >= 1:
            self._heat_water()
        else:
            raise ValueError("Not enough water to make coffee!")
        if self.beans_quantity >= 1:
            self._grind_beans()
        else:
            raise ValueError("Not enough beans to make coffee!")
        self._pump_water()
        self._eject_waste()
        print("Coffee made!")


class GroundCoffeeMachine(CoffeeMachine):
    """
    A class describing a ground coffee machine

    Properties:
        ground_coffee_level: int, max value 10, level of ground coffee

    Methods:
        make_ground_coffee: makes the coffee without grinding beans
    """
    def __init__(self):
        """ Initialises the properties """
        super().__init__()
        self._ground_coffee_level = 10

    @property
    def ground_coffee_level(self):
        """ ground_coffee_level getter """
        return self._ground_coffee_level

    @ground_coffee_level.setter
    def ground_coffee_level(self, new_value):
        """
        ground_coffee_level setter method

        Args:
            new_value: int specifying the quantity

        Returns:
            None

        Raises:
            ValueError: if the value is more than 10
            ValueError: if the value is not an int
        """
        if isinstance(new_value, int):
            if new_value > 10:
                raise ValueError("The new value must be 10 or less!")
            else:
                self._ground_coffee_level = new_value
        else:
            raise ValueError("The new value must be a number!")

    def make_coffee(self):
        """ Makes the ground coffee """
        if self.water_level >= 1:
            self._heat_water()
        else:
            raise ValueError("Not enough water to make coffee!")

        self._pump_water()
        self._eject_waste()
        print("Ground coffee made!")


print("Making regular coffee")
my_coffee_machine = CoffeeMachine()

print("Making ground coffee")
my_ground_coffee_machine = GroundCoffeeMachine()

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
    
    def _pierce_pod(self):
        """ Pierces the foil pod """
        print("Pod successfully pierced")
    
    def _eject_waste(self):
        """ ejects the used pod """
        print("Pod ejected")
        
    def make_coffee(self):
        """ makes a coffee-like drink """
        self._heat_water()
        self._pierce_pod()
        self._pump_water()
        self._eject_waste()
        print("Made a coffee-like drink!")
       

my_pod_coffee_machine = PodCoffeeMachine()
my_pod_coffee_machine.make_coffee()
