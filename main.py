import random
import time

class Pet:
    def __init__(self, name: str, pet_type: str):
        self.name = name
        self.pet_type = pet_type
        self.hunger = 50  # голод (0-100)
        self.energy = 50  # энергия (0-100)
        self.happiness = 50  # счастье (0-100)

    def __str__(self):
        return f"{self.name} - {self.pet_type}\nГолод: {self.hunger}/100\nЭнергия: {self.energy}/100\nСчастье: {self.happiness}/100"

    def feed(self):
        if self.hunger < 100:
            self.hunger += 20
            self.happiness += 5
            print(f"{self.name} поел(а) и стал(а) счастливее!")
        else:
            print(f"{self.name} сейчас не голоден(на).")
        self._update_state()

    def play(self):
        if self.energy > 20 and self.hunger > 20:
            self.energy -= 20
            self.hunger -= 15
            self.happiness += 10
            print(f"{self.name} поиграл(а) и повеселел(а)!")
        else:
            print(f"{self.name} слишком устал(а) или голоден(на), чтобы играть.")
        self._update_state()

    def sleep(self):
        print(f"{self.name} уснул(а)...")
        time.sleep(1)  # симуляция сна
        self.energy = min(100, self.energy + 30)
        self.hunger -= 10
        print(f"{self.name} отдохнул(а) и теперь полон(а) сил!")
        self._update_state()

    def _update_state(self):
        # Этот метод обновляет состояния питомца и проверяет на возможные риски
        if self.hunger <= 0:
            print(f"{self.name} очень голоден(на)! Накормите его(её)!")
        elif self.hunger > 100:
            self.hunger = 100

        if self.energy <= 0:
            print(f"{self.name} вымотан(а)! Ему(ей) нужно отдохнуть.")
        elif self.energy > 100:
            self.energy = 100

        if self.happiness <= 0:
            print(f"{self.name} грустит. Поиграйте с ним(ней)!")
        elif self.happiness > 100:
            self.happiness = 100

    def live_one_day(self):
        # Метод симулирует один день жизни питомца
        for _ in range(3):  # Три действия в течение дня
            action = random.choice([self.feed, self.play, self.sleep])
            action()
            print(self)
            print("-" * 20)

# Пример использования
my_pet = Pet(name="Барсик", pet_type="Котик")
my_pet.live_one_day()
