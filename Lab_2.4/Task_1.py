class Animal:
    """ Базовый класс животного. """
    def __init__(self, species: str, name: str, age: int) -> None:
        """
        Создание и подготовка к работе объекта "Животное"

        :param species: Название вида
        :param name: Кличка животного
        :param age: Возраст животного
        """
        self.species = species
        self.name = name
        if age < 0:
            raise ValueError("Возраст животного не может быть отрицательным числом")
        self.age = age

    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        return f"{self.species} {self.name} {self.age}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(species='{self.species!r}', name='{self.name!r}', age={self.age!r})"

    def make_a_sound(self) -> str:
        """
        Метод, описывающий издаваемый животным звук
        :return: Звук животного
        """
        return "Неизвестный звук"

    def set_weight(self, weight: float) -> None:
        """
        Устанавливает вес животного.
        :param weight: Вес животного
        """
        if weight < 0:
            raise ValueError("Вес не может быть отрицательным.")
        ...


class Dog (Animal):
    """Класс для представления собак, наследуется от Животное."""

    def __init__(self, species: str, breed: str, name: str, age: int) -> None:
        """Инициализирует объект Собака, расширяя конструктор Животное."""
        super().__init__(species, name, age)
        self.breed = breed

    def __str__(self) -> str:
        """Перегружает метод __str__ для добавления информации о породе."""

        return f"{self.species} {self.breed} {self.name} {self.age}"

    def __repr__(self) -> str:
        """Перегружает метод __repr__ для добавления информации о породе."""
        return f"{self.__class__.__name__}(species='{self.species!r}', breed='{self.breed!r} name='{self.name!r}', " \
               f"age={self.age!r})"

    def make_a_sound(self) -> str:
        """Перегружает метод make_a_sound для собак."""
        return "Гав!"


if __name__ == "__main__":
    # Write your solution here
    pass
