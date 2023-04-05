class Dog:
    Biology_classification = 'Animals'
    def __init__(self, name, weight, color):
        self.__name = name
        self.weight = weight
        self.color = color

    def run(self):
        return "I can run"

    def get_name(self):
        return  f"Hello! My name is {self.__name}"

    def __set_name__(self, new_name):
        self.__name = new_name



'''Create a New Object'''

dog1 = Dog("Bobik", 3, 'brown')
# print(dog1.name)
# print(dog1.get_name())
# print(dog1.run())

# print(dog1.Biology_classification)

dog2 = Dog('Rex', 5, 'black')
print(dog2.Biology_classification)
print(dog2.get_name())
# print(dog2.__name)
# print(dog2.set_name("Snoopy"))
print(dog2.get_name())
print(dog2.__dict__)
print(dog2._Dog__name)

# print(dog2.__dict__)
# dog2.name = 'Snoopy'
# print(dog2.name)
# print(dog2.__dict__)


class Pitbull(Dog):

    def __init__(self, name, weight, color, passport):
        super().__init__(name, weight, color)
        self.passport = passport


    def give_a_paw(self):
        return 'I can give you my paw!'

    def run(self):
        return "I can run fast!"

dog3 = Pitbull('Lassie', 8, 'black', 'type1')
# print(dog3.passport)
# print(dog3.get_name())
# print(dog3.give_a_paw())
# print(dog3.run())


