class Human:
    def __init__(self, name):
        self.name = name

class Car:
    def __init__(self, model):
        self.model = model
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def info(self):
        print(f"Auto : {self.model}")
        if self.passengers:
            print("Зараз присутні")
            for p in self.passengers:
                print(p.name)
        else:
            print("Пасажири відсутні")


human1 = Human("Sergiy")
human2 = Human("Anna")

car = Car("Tesla Model 13")
car.add_passenger(human1)
car.add_passenger(human1)
car.add_passenger(human1)
car.add_passenger(human1)
car.add_passenger(human1)









class Human:
    def __init__(self, name):
        self.name = name

class Car:
    def __init__(self, model):
        self.model = model
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def info(self):
        print(f"Auto : {self.model}")
        if self.passengers:
            print("Зараз присутні")
            for p in self.passengers:
                print(p.name)
        else:
            print("Пасажири відсутні")


human1 = Human("Sergiy")
human2 = Human("Anna")

car = Car("Tesla Model 13")
car.add_passenger(human1)
car.add_passenger(human1)
car.add_passenger(human1)
car.add_passenger(human1)
car.add_passenger(human1)