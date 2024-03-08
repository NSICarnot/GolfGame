import ursina


class Ball:
    def __init__(self):
        self.__radius: float = 0.00215  # In meters
        self.__mass: float = 45.93  # In grams
        self.__static_force_coef: float = .30  # In Newtons
        self.__kinetic_force_coef: float = .26  # In Newtons
