import json
import csv
from pathlib import Path

from src.lib.io_txt_csv import ensure_parent_dir

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Конвертирует JSON (список словарей) в CSV.

    Требования:
        - JSON должен содержать список объектов (list of dict).
        - Пропущенные ключи заполняются пустыми строками.
        - Кодировка UTF-8.
        - Заголовок формируется по ключам первого объекта 
          (или алфавитный порядок — по решению автора).

    Параметры:
        json_path (str): путь к входному JSON-файлу.
        csv_path (str): путь к выходному CSV-файлу.

    Исключения:
        FileNotFoundError — при отсутствии входного файла.
        ValueError — если JSON пустой или имеет неподдерживаемую структуру.
    """
    
    json_path = Path(json_path)
    csv_path = Path(csv_path)

    if not json_path.exists():
        raise FileNotFoundError(f"JSON-файл '{json_path}' не найден.")

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list) or not all(isinstance(x, dict) for x in data):
        raise ValueError("JSON должен быть списком словарей.")

    if not data:
        raise ValueError("JSON-файл пуст.")

    # Собираем все ключи (чтобы заполнить пропуски пустыми строками)
    fieldnames = sorted({key for item in data for key in item.keys()})

    ensure_parent_dir(csv_path)
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow({k: row.get(k, "") for k in fieldnames})

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Конвертирует CSV в JSON (список словарей).

    Требования:
        - Первая строка CSV — заголовок.
        - Все значения записываются как строки.
        - json.dump(..., ensure_ascii=False, indent=2)

    Параметры:
        csv_path (str): путь к входному CSV-файлу.
        json_path (str): путь к выходному JSON-файлу.

    Исключения:
        FileNotFoundError — если CSV-файл не найден.
        ValueError — если файл пустой или не содержит заголовка.
    """

    csv_path = Path(csv_path)
    json_path = Path(json_path)

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV-файл '{csv_path}' не найден.")

    with csv_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        raise ValueError("CSV-файл пуст.")

    ensure_parent_dir(json_path)
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)