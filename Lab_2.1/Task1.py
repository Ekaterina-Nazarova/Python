import doctest


class Theater:
    def __init__(self, performance: str, vacant_seats: int):
        """
        Создание и подготовка к работе объекта "Театр"

        :param performance: Название спектакля
        :param vacant_seats: Количество свободных мест

        Примеры:
        >>> theater = Theater("Щелкунчик", 20)  # инициализация экземпляра класса
        """
        if not isinstance(performance, str):
            raise TypeError("Название спектакля должно быть типа str")
        self.performance = performance

        if not isinstance(vacant_seats, int):
            raise TypeError("Количество свободных мест должно быть int")
        if vacant_seats < 0:
            raise ValueError("Количество свободных мест не может быть отрицательным числом")
        self.vacant_seats = vacant_seats

    def is_vacant_seats(self) -> bool:
        """
        Функция которая проверяет есть ли свободные места

        :return: Есть ли свободные места

        Примеры:
        >>> theater = Theater("Щелкунчик", 20)
        >>> theater.is_vacant_seats()
        """
        ...

    def buy_seats(self, tickets: int) -> None:
        """
        Покупка билетов.
        :param tickets: Количество покупаемых билетов.

        :raise ValueError: Если количество покупаемых билетов превышает количество свободных мест, то вызываем ошибку
        Примеры:
        >>> theater = Theater("Щелкунчик", 20)
        >>> theater.buy_seats(200)
        """
        if not isinstance(tickets, int):
            raise TypeError("Количество билетов должно быть типа int")
        if tickets < 0:
            raise ValueError("Количество билетов не может быть отрицательным числом")
        ...


class SocialMediaPlatform:
    def __init__(self, name: str, user_count: int):
        """
        Создание и подготовка к работе объекта "Социальная сеть"

        :param name: Название соц.сети
        :param user_count: Количество пользователей

        Примеры:
        >>> social_media_platform = SocialMediaPlatform("VK", 3100000)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название соц.сети должно быть типа str")
        self.name = name

        if not isinstance(user_count, int):
            raise TypeError("Количество пользователей должно быть int")
        if user_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным числом")
        self.user_count = user_count

    def add_users(self, accounts: int) -> None:
        """
        Добавление пользователей на платформу.
        :param accounts: Количество новых пользователей
        :return: Новое количество пользователей


        Примеры:
        >>> social_media_platform = SocialMediaPlatform("VK", 3100000)
        >>> social_media_platform.add_users(20000)
        """
        if not isinstance(accounts, int):
            raise TypeError("Количество новых пользователей должно быть типа int")
        if accounts < 0:
            raise ValueError("Количество новых пользователей не может быть отрицательным числом")
        ...

    def remove_users(self, come_off: int) -> None:
        """
        Удаление пользователей с платформы

        :param come_off: Количество отписавшихся аккаунтов
        :raise ValueError: Если количество отписавшихся аккаунтов превышает количество пользователей,
        то возвращается ошибка.

        :return: Новое количество пользователей

        Примеры:
        >>> social_media_platform = SocialMediaPlatform("VK", 3100000)
        >>> social_media_platform.remove_users(20000)
        """
        if not isinstance(come_off, int):
            raise TypeError("Количество отписавшихся аккаунтов должно быть типа int")
        if come_off < 0:
            raise ValueError("Количество отписавшихся аккаунтов не может быть отрицательным числом")
        ...


class Transport:
    def __init__(self, fuel_volume: float, fuel_consumption: float, max_fuel_volume: float):
        """
        Создание и подготовка к работе объекта "Транспорт"

        :param fuel_volume: Количество топлива в баке
        :param fuel_consumption: Расход топлива на 100 километров
        :param max_fuel_volume: Максимальное количество топлива

        Примеры:
        >>> transport = Transport(19.5, 8.6, 25)  # инициализация экземпляра класса
        """
        if not isinstance(fuel_volume, (int, float)):
            raise TypeError("Количество в баке должен быть типа int или float")
        if fuel_volume < 0:
            raise ValueError("Количество топлива в баке не может быть отрицательным числом")
        self.fuel_volume = fuel_volume

        if not isinstance(fuel_consumption, (int, float)):
            raise TypeError("Расход топлива должен быть int или float")
        if fuel_consumption <= 0:
            raise ValueError("Расход топлива должен быть положительным числом")
        self.fuel_consumption = fuel_consumption

        if not isinstance(max_fuel_volume, (int, float)):
            raise TypeError("Максимальное количество топлива в баке должен быть типа int или float")
        if max_fuel_volume <= 0:
            raise ValueError("Максимальное количество топлива в баке должно быть положительным числом")
        self.max_fuel_volume = max_fuel_volume

    def add_fuel_to_transport(self, liters: float) -> None:
        """
        Добавление топлива в бак транспорта.
        :param liters: Объем добавляемого топлива

        :raise ValueError: Если количество добавляемого топлива превышает максимальное количество топлива,
        то вызываем ошибку
        :return: Объем реально добавляемого топлива

        Примеры:
        >>> transport = Transport(19.5, 8.6, 25)
        >>> transport.add_fuel_to_transport(200)
        """
        if not isinstance(liters, (int, float)):
            raise TypeError("Объем добавляемого топлива должен быть типа int или float")
        if liters < 0:
            raise ValueError("Объем добавляемого топлива не может быть отрицательным числом")
        ...

    def distance_calculation(self, speed: float) -> None:
        """
        Подсчет, на сколько километров сможет уехать транспорт
        при данном количестве топлива в баке и заданной скорости без дозаправки

        :param speed: Заданная скорость движения

        :return: Расстояние в километрах

        Примеры:
        >>> transport = Transport(19.5, 8.6, 25)
        >>> transport.distance_calculation(120)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
