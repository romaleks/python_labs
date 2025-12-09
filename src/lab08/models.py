from dataclasses import dataclass
from datetime import datetime, date
from typing import Any, Dict


@dataclass
class Student:
    """
    Модель студента.

    Поля:
        fio: ФИО студента
        birthdate: дата рождения в формате YYYY-MM-DD
        group: учебная группа, напр. SE-01
        gpa: средний балл в диапазоне 0..5
    """

    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        # Проверка формата даты
        self.gpa = float(self.gpa)
        
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                f"Некорректный формат birthdate: {self.birthdate}. Используйте YYYY-MM-DD."
            )

        # Проверка GPA
        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa должно быть в диапазоне [0; 5]")

    def age(self) -> int:
        """
        Возвращает количество полных лет.
        """
        b = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        years = today.year - b.year
        # Если ДР ещё не было в этом году — вычитаем один
        if (today.month, today.day) < (b.month, b.day):
            years -= 1
        return years

    def to_dict(self) -> Dict[str, Any]:
        """
        Сериализация объекта студента в словарь.
        """
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Student":
        """
        Создание объекта Student из словаря.
        """
        required = {"fio", "birthdate", "group", "gpa"}

        if not required.issubset(data):
            missing = required - data.keys()
            raise ValueError(f"Отсутствуют поля: {', '.join(missing)}")

        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=float(data["gpa"]),
        )

    def __str__(self) -> str:
        """
        Красивый вывод студента.
        """
        return f"{self.fio} ({self.group}), GPA={self.gpa}, возраст={self.age()}"
