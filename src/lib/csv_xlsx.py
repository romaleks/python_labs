from pathlib import Path
import csv
from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в Excel-файл (.xlsx).

    Требования:
        - Первая строка CSV используется как заголовок.
        - Лист называется 'Sheet1'.
        - Ширина колонок подбирается автоматически: 
          max(длина текста, 8 символов).
        - Используется библиотека openpyxl.
        - Кодировка входного CSV — UTF-8.

    Параметры:
        csv_path (str): путь к CSV-файлу.
        xlsx_path (str): путь к создаваемому XLSX.

    Исключения:
        FileNotFoundError — входной файл отсутствует.
        ValueError — CSV пустой или структура неверная.
    """

    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV-файл '{csv_path}' не найден.")

    # Читаем CSV
    with csv_file.open(encoding="utf-8") as f:
        reader = list(csv.reader(f))
        if not reader:
            raise ValueError("Пустой CSV-файл")

    # Создаём Excel-файл
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    # Добавляем строки
    for row in reader:
        ws.append(row)

    # Автоширина колонок (минимум 8)
    for col in ws.columns:
        max_len = 0
        col_letter = col[0].column_letter  # A, B, C...
        for cell in col:
            val = str(cell.value) if cell.value is not None else ""
            max_len = max(max_len, len(val))
        ws.column_dimensions[col_letter].width = max(max_len + 2, 8)

    # Сохраняем результат
    wb.save(xlsx_path)