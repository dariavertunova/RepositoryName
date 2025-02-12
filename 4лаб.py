class Animal:
    """
    Базовый класс, представляющий животное.
    """

    def __init__(self, name: str, species: str, weight: float):
        """
        Args:
            name (str): Имя животного.
            species (str): Вид животного.
            weight (float): Вес животного.
        """
        self.name = name
        self.species = species
        self.weight = weight

    def make_sound(self) -> str:
        """
        Returns:
            str: Звук животного.
        """
        return "Generic animal sound"

    def eat(self, food: str) -> None:
        """
        Args:
            food (str): Тип пищи.
        """
        print(f"{self.name} the {self.species} is eating {food}.")

    def __str__(self) -> str:
        """
        Returns:
            str: Строковое представление животного.
        """
        return f"{self.name} is a {self.species} weighing {self.weight} kg."

    def __repr__(self) -> str:
        """
        Returns:
            str: Строковое представление объекта Animal.
        """
        return f"Animal(name='{self.name}', species='{self.species}', weight={self.weight})"

class Dog(Animal):
    """
    Дочерний класс, представляющий собаку. Наследуется от Animal.
    """

    def __init__(self, name: str, breed: str, weight: float, is_trained: bool = False):
        """
        Args:
            name (str): Имя собаки.
            breed (str): Порода собаки.
            weight (float): Вес собаки.
            is_trained (bool): Обучена ли собака.
        """
        super().__init__(name, species="Dog", weight=weight)
        self.breed = breed
        self.is_trained = is_trained

    def make_sound(self) -> str:
        """
        Returns:
            str: Лай собаки.
        """
        return "Woof!"

    def fetch(self, item: str) -> None:
        """
            item (str): Предмет, который собака приносит.
        """
        print(f"{self.name} the {self.breed} is fetching the {item}.")

    def train(self) -> None:
        """
        Метод для обучения собаки.
        """
        if not self.is_trained:
            print(f"Training {self.name}...")
            self.is_trained = True
            print(f"{self.name} is now trained!")
        else:
            print(f"{self.name} is already trained.")

    def __str__(self) -> str:
        """
        Returns:
            str: Строковое представление собаки.
        """
        return f"{self.name} is a {self.breed} Dog weighing {self.weight} kg."

    def __repr__(self) -> str:
        """
        Returns:
            str: Строковое представление объекта Dog.
        """
        return f"Dog(name='{self.name}', breed='{self.breed}', weight={self.weight}, is_trained={self.is_trained})"

if __name__ == "__main__":
    animal = Animal(name="Generic", species="Animal", weight=10.0)
    print(animal)
    print(repr(animal))
    print(animal.make_sound())
    animal.eat("food")

    dog = Dog(name="Buddy", breed="Golden Retriever", weight=25.0)
    print(dog)
    print(repr(dog))
    print(dog.make_sound())
    dog.eat("dog food")
    dog.fetch("ball")
    dog.train()
    print(dog)