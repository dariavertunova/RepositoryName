import doctest
from abc import ABC, abstractmethod


class AbstractContainer(ABC):
    """
    Абстрактный класс для контейнеров.
    """
    
    @abstractmethod
    def is_empty(self) -> bool:
        """
        Проверяет, пустой ли контейнер.

        :return: True, если контейнер пустой, иначе False.

        Примеры:
        >>> container = ConcreteContainer(100, 0)
        >>> container.is_empty()
        True
        """
        ...

    @abstractmethod
    def add_item(self, amount: float) -> None:
        """
        Добавляет предмет в контейнер.

        :param amount: Объем добавляемого предмета
        :raise ValueError: Если добавляемый объем превышает свободное место в контейнере.

        Примеры:
        >>> container = ConcreteContainer(100, 0)
        >>> container.add_item(50)
        """
        ...

    @abstractmethod
    def remove_item(self, amount: float) -> None:
        """
        Извлекает предмет из контейнера.

        :param amount: Объем извлекаемого предмета
        :raise ValueError: Если извлекаемый объем превышает количество предметов в контейнере.

        Примеры:
        >>> container = ConcreteContainer(100, 50)
        >>> container.remove_item(20)
        """
        ...


class ConcreteContainer(AbstractContainer):
    def __init__(self, capacity: float, occupied: float):
        """
        Создание и подготовка к работе объекта "Контейнер"

        :param capacity: Общий объем контейнера
        :param occupied: Объем занимаемого пространства

        Примеры:
        >>> container = ConcreteContainer(100, 0)
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError("Объем контейнера должен быть типа int или float")
        if capacity <= 0:
            raise ValueError("Объем контейнера должен быть положительным числом")

        self.capacity = capacity

        if not isinstance(occupied, (int, float)):
            raise TypeError("Занимаемый объем должен быть int или float")
        if occupied < 0 or occupied > capacity:
            raise ValueError("Занимаемый объем не может быть отрицательным или превышать общий объем")

        self.occupied = occupied

    def is_empty(self) -> bool:
        return self.occupied == 0

    def add_item(self, amount: float) -> None:
        if not isinstance(amount, (int, float)):
            raise TypeError("Добавляемый объем должен быть типа int или float")
        if amount <= 0:
            raise ValueError("Добавляемый объем должен быть положительным числом")

        if self.occupied + amount > self.capacity:
            raise ValueError("Недостаточно места для добавления указанного объема")

        self.occupied += amount

    def remove_item(self, amount: float) -> None:
        if not isinstance(amount, (int, float)):
            raise TypeError("Извлекаемый объем должен быть типа int или float")
        if amount <= 0:
            raise ValueError("Извлекаемый объем должен быть положительным числом")

        if amount > self.occupied:
            raise ValueError("Недостаточно объема для извлечения указанного количества")

        self.occupied -= amount


class AbstractTree(ABC):
    """
    Абстрактный класс для деревьев.
    """

    @abstractmethod
    def grow(self, height_increase: float) -> None:
        """
        Увеличивает высоту дерева.

        :param height_increase: Увеличение высоты дерева
        :raise ValueError: Если увеличение высоты отрицательное.

        Примеры:
        >>> tree = ConcreteTree(5)
        >>> tree.grow(2)
        """
        ...

    @abstractmethod
    def shed_leaves(self) -> None:
        """
        Сбрасывает листья с дерева.

        Примеры:
        >>> tree = ConcreteTree(5)
        >>> tree.shed_leaves()
        """
        ...


class vase:
    def __init__(self, capacity_volume: float, occupied_volume: float, height: float):
        """
        Создание и подготовка к работе объекта "Ваза"
        :param capacity_volume: Объем вазы
        :param occupied_volume: Объем занимаемой жидкости
        :param height: Высота вазы
        Примеры:
        >>> vase = Vase(3, 0, 16)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем вазы должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем вазы должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(height, (int, float)):
            raise TypeError("Высота вазы должна быть int или float")
        if height <= 0:
            raise ValueError("Высота вазы должна быть положительным числом")
        self.height = height

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть типа int или float")
        if occupied_volume <= 0:
            raise ValueError("Количество жидкости должно быть положительным числом")
        self.occupied_volume = occupied_volume

    def is_empty_vase(self) -> bool:
        """
        Функция которая проверяет есть ли в вазе вода
        :return: Есть ли в вазе вода
        Примеры:
        >>> vase = Vase(2, 0, 10)
        >>> vase.is_empty_vase()
        """
        ...

    def put_flower_to_vase(self, fl_height: float) -> None:
        """
        Размещение цветка в вазе.
        :param fl_height: Выста цветка, который ставят в вазу
        :raise ValueError: Если высота цветка превышает высоту вазы, то вызываем ошибку
        Примеры:
        >>> vase = Vase(3, 6, 17)
        >>> vase.put_flower_to_vase(15)
        """
        if not isinstance(fl_height, (int, float)):
            raise TypeError("Выста цветка должна быть типа int или float")
        if fl_height <= 0:
            raise ValueError("Выста цветка должна быть положительным числом")
        ...


if __name__ == "__Лабораторная_1__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации