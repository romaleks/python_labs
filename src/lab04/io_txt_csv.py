import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Открывает текстовый файл и возвращает его содержимое как строку.
    Если нужно использовать другую кодировку (например, Windows-1251), 
    можно вызвать так:
        text = read_text("data/file.txt", encoding="cp1251")

    Аргументы:
        path (str | Path): путь к файлу.
        encoding (str, optional): кодировка файла. По умолчанию "utf-8".
            Можно указать другую, например encoding="cp1251".

    Исключения:
        FileNotFoundError — если файл не найден.
        UnicodeDecodeError — если файл не удаётся прочитать в данной кодировке.

    Возвращает:
        str: содержимое файла.
    """
    p = Path(path)
    return p.read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path) -> None:
    """
    Создаёт родительские директории для файла, если их нет.
    """
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def write_csv(
    rows: Iterable[Sequence],
    path: str | Path,
    header: tuple[str, ...] | None = None
) -> None:
    """
    Создаёт CSV-файл с разделителем ",".
    Если передан header — записывает его первой строкой.
    Проверяет, что все строки rows имеют одинаковую длину, иначе ValueError.

    Аргументы:
        rows (Iterable[Sequence]): последовательность строк (списки или кортежи).
        path (str | Path): путь к создаваемому файлу.
        header (tuple[str, ...] | None): необязательная строка заголовков.

    Исключения:
        ValueError — если строки в rows имеют разную длину.
    """
    rows = list(rows)
    ensure_parent_dir(path)

    # Проверяем равенство длины строк (если не пусто)
    if rows:
        lengths = {len(r) for r in rows}
        if len(lengths) > 1:
            raise ValueError("Все строки в rows должны иметь одинаковую длину")

    p = Path(path)
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        for r in rows:
            writer.writerow(r)
