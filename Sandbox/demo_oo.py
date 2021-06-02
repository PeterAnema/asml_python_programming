class Person:

    # class-wide attribute
    MAXIMUM_AGE = 110

    def __init__(self, name, residence = 'unknown'):
        self._lastname = name
        self._residence = residence

    def tell(self):
        print(f'My name is {self._lastname} and I live in {self._residence}')

    def move(self, new_residence):
        self._residence = new_residence

    def get_name(self):
        return self._lastname

# =====================================================

p1 = Person('Peter')
p1.tell()

p2 = Person('Martin', 'Eindhoven')
p2.tell()

p1.move('Utrecht')
p1.tell()

Person.MAXIMUM_AGE = 120
print(Person.MAXIMUM_AGE)


