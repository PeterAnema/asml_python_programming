class Car:

    def __init__(self, make, type, color):
        self._make = make
        self._type = type
        self._color = color
        self._mileage = 0
        self._started = False

    def info(self):
        print( f'This great {self._color} {self._make} {self._type} as driven {self._mileage}km.' )
        if self._started:
            print( f'The engine is still running.')

    def drive(self, km):
        if self._started:
            self._mileage += km
        else:
            print('Please start your car first.')

    def start(self):
        self._started = True

    def stop(self):
        self._started = False

# -------------------------------------------------------

my_car = Car('Renault', 'Megane', 'metalic brown')

my_car.start()
my_car.drive(200)
my_car.info()
