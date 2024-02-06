import doctest

class PowerSupply:
    def __init__(self, power_generation_per_hour: float, cost_per_energy_unit: float):
        """
        Инициализация объекта "PowerSupply"

        :param power_generation_per_hour: Кол-во единиц энергии, вырабатываемой за час работы
        :param cost_per_energy_unit: Стоимость одной единицы энергии
        """
        self.power_generation_per_hour = power_generation_per_hour
        self.cost_per_energy_unit = cost_per_energy_unit

    def __str__(self) -> str:
        """
        Функция вывода класса объекта в читаемом виде
        """
        return f'Объект класса {self.__class__.__name__}'

    def __repr__(self) -> str:
        """
        Функция вывода инструкции для создания объекта класса
        """
        return f'{self.__class__.__name__}(power_generation_per_hour={self.power_generation_per_hour}, cost_per_energy_unit={self.cost_per_energy_unit})'

    def hourly_cost(self) -> float:
        """
        Функция для вычисления стоимости работы станции

        :return: Стоимость работы за каждый час
        """
        return self.power_generation_per_hour *  self.cost_per_energy_unit

    def fuel_consumption_per_hour(self) -> float:
        """
        Функция для вычисления кол-ва потребляемого топлива

        :return: Кол-во единиц потребляемого топлева в час
        """
        ...

class NuclearReactor(PowerSupply):
    def __init__(self, power_generation_per_hour: float, cost_per_energy_unit: float, coolant: str, reactor_type: str):
        """
        Объект класса "NuclearReactor"

        :param power_generation_per_hour: Кол-во единиц энергии, вырабатываемой за час работы
        :param cost_per_energy_unit: Стоимость одной единицы энергии
        :param coolant: Субстнация, используемая для охлаждения реактора
        :param reactor_type: Тип реактора (Fission/Fusion)
        """
        super().__init__(power_generation_per_hour, cost_per_energy_unit)
        self.coolant = coolant
        self.reactor_type = reactor_type

    def __repr__(self) -> str:
        """
        Функция вывода инструкции для создания объекта класса
        """
        return f'{self.__class__.__name__}(power_generation_per_hour={self.power_generation_per_hour}, cost_per_energy_unit={self.cost_per_energy_unit}, coolant={self.coolant!r}, reactor_type={self.reactor_type!r})'

    def fuel_consumption_per_hour(self) -> float:
        """
        Функция для вычисления кол-ва потребляемого топлива
        Перегружает метод базового класса для учета конкретного вида топлива

        :return: Кол-во единиц потребляемого топлева в час
        """
        ...

class CoalPlant(PowerSupply):
    def __init__(self, power_generation_per_hour: float, cost_per_energy_unit: float, emissions_per_energy_unit: float):
        """
        Объект класса "CoalPlant"

        :param power_generation_per_hour: Кол-во единиц энергии, вырабатываемой за час работы
        :param cost_per_energy_unit: Стоимость одной единицы энергии
        :param emissions_per_energy_unit: Объём выделения углекислого газа на единицу энергии
        """
        super().__init__(power_generation_per_hour, cost_per_energy_unit)
        self.emissions_per_energy_unit = emissions_per_energy_unit

    def __repr__(self) -> str:
        """
        Функция вывода инструкции для создания объекта класса
        """
        return f'{self.__class__.__name__}(power_generation_per_hour={self.power_generation_per_hour}, cost_per_energy_unit={self.cost_per_energy_unit}, emissions_per_energy_unit={self.emissions_per_energy_unit})'

    def fuel_consumption_per_hour(self) -> float:
        """
        Функция для вычисления кол-ва потребляемого топлива
        Перегружает метод базового класса для учета конкретного вида топлива

        :return: Кол-во единиц потребляемого топлева в час
        """
        ...


if __name__ == "__main__":
    doctest.testmod()

    nuclear = NuclearReactor(500, 10.2, "Water", "Fission")
    coal = CoalPlant(300, 8.43, 120)

    print(nuclear)
    print(coal.__repr__())
    print(nuclear.hourly_cost())

