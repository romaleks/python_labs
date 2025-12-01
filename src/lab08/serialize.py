import json
from pathlib import Path
from typing import List

from .models import Student
from ..lib.io_txt_csv import ensure_parent_dir


def students_to_json(students: List[Student], path: str) -> None:
    """
    Сохраняет список объектов Student в JSON-файл.

    Args:
        students: список студентов
        path: путь к выходному JSON
    """
    data = [s.to_dict() for s in students]

    p = Path(path)
    ensure_parent_dir(p)

    with p.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str) -> List[Student]:
    """
    Загружает список студентов из JSON-файла.

    Returns:
        list[Student]
    """
    p = Path(path)

    if not p.exists():
        raise FileNotFoundError(f"Файл не найден: {p}")

    with p.open(encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("JSON должен содержать массив объектов")

    students = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Каждая запись JSON должна быть объектом")
        students.append(Student.from_dict(item))

    return students
