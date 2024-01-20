import doctest
from typing import Union

class Microphone:
    def __init__(self, sensitivity: Union[int, float], mute: bool):
        """
           Создание и подготова к работе объекта "Микрофон"

           :param sensitivity: Чувствительность микрофона в процентах
           :param mute: Состояние заглушения микрофона (включено/выключено)

           Примеры:
           >>> microphone = Microphone(50, True)
           """
        self.sensitivity = 0
        self.sensitivity = self.change_sensitivity(sensitivity)

        if not isinstance(mute, bool):
            raise TypeError("mute должен иметь тип bool")
        self.mute = mute

    def unmute(self) -> None:
        """
        Функция для изменения состояния заглушения микрофона

        Примеры:
        >>> microphone = Microphone(50, True)
        >>> microphone.unmute()
        """
        ...

    def change_sensitivity(self, sensitivity: Union[int, float]) -> None:
        """
        Функция для изменения чувствительности микрофона

        :param sensitivity: Чувствительность микрофона в процентах
        :raise ValueError: Если чувствительность меньше 0% или больше 100%, то возвращается ошибка

        Примеры:
        >>> microphone = Microphone(50, True)
        >>> microphone.change_sensitivity(75)
        """
        if not isinstance(sensitivity, (int, float)):
            raise TypeError("sensitivity должен иметь тип int или float")
        if not 0 <= sensitivity <= 100:
            raise ValueError("Чувствительность должна быть в диапазоне от 0 до 100")
        ...

class Plate:
    def __init__(self, material: str, height: float, width: float):
        """
        Создание и подготова к работе объекта "Пластина"

        :param material: Материал из которого изготовлена пластина
        :param height: Высота пластины в метрах
        :param width: Ширина пластины в метрах

        :raise ValueError: Если высота или ширина пластины отрицательные, то возвращает ошибку

        Примеры:
        >>> plate = Plate("Железо", 50.0, 20.0)
        """
        if not isinstance(material, str):
            raise TypeError("material должен иметь тип str")
        self.material = material

        if not isinstance(height, float):
            raise TypeError("height должен иметь тип float")
        if height < 0:
            raise ValueError("Высота пластины не может быть отрицательной")
        self.height = height

        if not isinstance(width, float):
            raise TypeError("width должен иметь тип float")
        if width < 0:
            raise ValueError("Ширина пластины не может быть отрицательной")
        self.width = width

    def area(self) -> float:
        """
        Функция находит площадь пластины

        :return: Площадь пластины

        Примеры:
         >>> plate = Plate("Железо", 50.0, 20.0)
         >>> plate.area()
        """
        ...

    def weight(self) -> float:
        """
        Функция находит вес пластины в зависимости от плотности выбранного материала

        :return: Вес пластины

        Примеры:
        >>> plate = Plate("Железо", 50.0, 20.0)
        >>> plate.weight()
        """
        ...

class CTFTeam:
    def __init__(self, name: str, tasks_completed: int, score: int):
        """
        Создание и подготовка к работе объекта "Команда CTF"

        :param name: Имя команды
        :param tasks_completed: Кол-во выполненных командой заданий
        :param score: Кол-во очков команды

        :raise ValueError: Если кол-во выполненных заданий или полученных очков отрицательное, то возвращает ошибку

        Примеры:
        >>> ctfteam = CTFTeam("1337", 2, 1000)
        """
        if not isinstance(name, str):
            raise TypeError("name должен иметь тип str")
        self.name = name

        if not isinstance(tasks_completed, int):
            raise TypeError("tasks_completed должен иметь тип int")
        if tasks_completed < 0:
            raise ValueError("Кол-во выполненных заданий не может быть отрицательным")
        self.tasks_completed = tasks_completed

        if not isinstance(score, int):
            raise TypeError("score должен иметь тип int")
        if score < 0:
            raise ValueError("Кол-во очков не может быть отрицательным")
        self.score = score

    def complete_tasks(self, amount: int) -> None:
        """
        Функция увеличивает значение кол-ва решенных командой заданий и добавляет соответствующее кол-во очков

        :param amount: Значение, на которое необходимо увеличить кол-во решенных заданий

        :raise ValueError: Если добавляемое кол-во заданий отрицательное, то возвращает ошибку

        Примеры:
        >>> ctfteam = CTFTeam("1337", 2, 1000)
        >>> ctfteam.complete_tasks(3)
        """
        if not isinstance(amount, int):
            raise TypeError("amount должен иметь тип int")
        if amount < 0:
            raise ValueError("Кол-во заданий не может быть отрицательным")
        ...

    def deduct_score(self, amount: int) -> None:
        """
        Функция вычитает очки за нарушение правил соревнования

        :param amount: Значение, на которое необходимо уменьшить очки

        :raise ValueError: Если вычитаемые очки отрицательные или команда в итоге будет иметь негативное значение очков, то возвращает ошибку

        Примеры:
        >>> ctfteam = CTFTeam("1337", 2, 1000)
        >>> ctfteam.deduct_score(500)
        """
        if not isinstance(amount, int):
            raise TypeError("amount должен иметь тип int")
        if amount < 0:
            raise ValueError("Кол-во заданий не может быть отрицательным")
        if (self.score - amount) < 0:
            raise ValueError("Очки команды не могут быть отрицательными")
        ...

if __name__ == "__main__":
    doctest.testmod()
