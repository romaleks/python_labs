"""
Скрипт для анализа текста и генерации отчёта в формате CSV.

Функции:
- Читает входной файл (по умолчанию data/input.txt)
- Нормализует и токенизирует текст (используя lib/text.py)
- Считает частоты слов и сортирует их (по частоте ↓, затем по слову ↑)
- Сохраняет результат в CSV (по умолчанию data/report.csv)
- Печатает краткое резюме в консоль

Пример запуска:
    python src/lab04/text_report.py
    python src/lab04/text_report.py --in data/in.txt --out data/out.csv
    python src/lab04/text_report.py --in data/in.txt --encoding cp1251

Если входной файл не существует — выводит сообщение и завершает работу с кодом 1.
Если файл пустой — создаётся report.csv только с заголовком word,count.
"""

import sys
import argparse
from pathlib import Path

from src.lib.io_txt_csv import read_text, write_csv
from src.lib.text import normalize, tokenize, count_freq, top_n


def main() -> None:
    """Точка входа в программу."""
    parser = argparse.ArgumentParser(
        description="Создание отчёта частот слов из текстового файла."
    )
    parser.add_argument(
        "--in",
        dest="input_path",
        default="data/lab04/input.txt",
        help="входной текстовый файл (по умолчанию data/input.txt)",
    )
    parser.add_argument(
        "--out",
        dest="output_path",
        default="data/lab04/report.csv",
        help="файл для сохранения отчёта (по умолчанию data/report.csv)",
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="кодировка входного файла (по умолчанию utf-8, можно cp1251 и др.)",
    )

    args = parser.parse_args()
    input_path = Path(args.input_path)
    output_path = Path(args.output_path)

    # Проверка существования входного файла
    if not input_path.exists():
        print(f"Ошибка: входной файл '{input_path}' не найден.", file=sys.stderr)
        sys.exit(1)

    # Чтение и анализ текста
    try:
        text = read_text(input_path, encoding=args.encoding)
    except UnicodeDecodeError:
        print(
            f"Ошибка: не удалось прочитать '{input_path}' в кодировке {args.encoding}.",
            file=sys.stderr,
        )
        sys.exit(1)

    freq = count_freq(tokenize(normalize(text)))
    sorted_rows = top_n(freq, len(freq))

    # Если текст пустой — пишем только заголовок
    if not sorted_rows:
        write_csv([], output_path, header=("word", "count"))
        print("Файл пустой. Создан отчёт только с заголовком.")
        return

    # Записываем результат в CSV
    write_csv(sorted_rows, output_path, header=("word", "count"))

    # Выводим краткое резюме
    total_words = sum(freq.values())
    unique_words = len(freq)
    top_5 = sorted_rows[:5]

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for w, c in top_5:
        print(f"  {w}: {c}")


if __name__ == "__main__":
    main()
