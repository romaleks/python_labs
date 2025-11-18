## Лабораторная работа 6

### Задание A

```python
import argparse
from pathlib import Path
from src.lib.text import normalize, tokenize, count_freq, top_n


def cmd_cat(path: Path, number_lines: bool) -> None:
    """
    Выводит содержимое текстового файла построчно.
    
    Параметры:
        path (str): путь к файлу.
        number_lines (bool): если True — добавляет нумерацию строк.
    
    Исключения:
        FileNotFoundError — если файл не существует.
    """

    if not path.exists():
        raise FileNotFoundError(f"Файл '{path}' не найден")

    with path.open(encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.rstrip("\n")
            if number_lines:
                print(f"{i}. {line}")
            else:
                print(line)


def cmd_stats(path: Path, top_k: int) -> None:
    """
    Анализирует текстовый файл и выводит статистику по словам:
    общее количество слов, уникальных слов и топ-N наиболее частых.

    Параметры:
        path (str): путь к текстовому файлу.
        top_n (int): сколько самых частых слов выводить.

    Использует функции нормализации, токенизации и подсчёта частот из lab03.

    Исключения:
        FileNotFoundError — если файл отсутствует.
        ValueError — если файл пуст.
    """

    if not path.exists():
        raise FileNotFoundError(f"Файл '{path}' не найден")

    text = path.read_text(encoding="utf-8")
    text = normalize(text)
    words = tokenize(text)
    freqs = count_freq(words)
    top = top_n(freqs, top_k)

    for word, count in top:
        print(f"{word}: {count}")


def main():
    """
    Точка входа CLI-утилиты.

    Создаёт парсер argparse, добавляет подкоманды:
        - cat   — вывод файла
        - stats — статистика слов
    
    Вызывает соответствующие функции в зависимости от аргументов.
    """

    parser = argparse.ArgumentParser(
        description="CLI-утилиты анализа текста: cat и stats"
    )
    subparsers = parser.add_subparsers(dest="command")

    # ---------------------- CAT ------------------------
    cat_p = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_p.add_argument("--input", required=True, help="Путь к файлу")
    cat_p.add_argument(
        "-n",
        action="store_true",
        help="Нумеровать строки"
    )

    # ---------------------- STATS ----------------------
    stats_p = subparsers.add_parser("stats", help="Частотный анализ текста")
    stats_p.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_p.add_argument(
        "--top",
        type=int,
        default=5,
        help="Количество наиболее частых слов (по умолчанию 5)",
    )

    args = parser.parse_args()

    # ------------ обработка подкоманд -----------------
    if args.command == "cat":
        cmd_cat(Path(args.input), args.n)

    elif args.command == "stats":
        cmd_stats(Path(args.input), args.top)

    else:
        parser.error("Не указана подкоманда (cat или stats)")


if __name__ == "__main__":
    main()
```

![Картинка 1](../../images/lab06/01.png)
![Картинка 2](../../images/lab06/02.png)

### Задание B 

```python
import argparse
import sys
from pathlib import Path

from src.lib.json_csv import json_to_csv, csv_to_json
from src.lib.csv_xlsx import csv_to_xlsx

def main() -> None:
    """
    CLI-утилита для конвертации файлов между форматами JSON, CSV и XLSX.

    Подкоманды:
        json2csv --in <json> --out <csv>
        csv2json --in <csv> --out <json>
        csv2xlsx --in <csv> --out <xlsx>

    Используются функции из lab05.
    """

    parser = argparse.ArgumentParser(description="Конвертер файлов: JSON↔CSV, CSV→XLSX")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # -----------------------
    # json2csv
    # -----------------------
    p_json2csv = subparsers.add_parser("json2csv", help="Преобразовать JSON → CSV")
    p_json2csv.add_argument("--in", dest="input", required=True, help="Входной JSON-файл")
    p_json2csv.add_argument("--out", dest="output", required=True, help="Выходной CSV-файл")

    # -----------------------
    # csv2json
    # -----------------------
    p_csv2json = subparsers.add_parser(
        "csv2json", help="Преобразовать CSV → JSON"
    )
    p_csv2json.add_argument("--in", dest="input", required=True, help="Входной CSV-файл")
    p_csv2json.add_argument("--out", dest="output", required=True, help="Выходной JSON-файл")

    # -----------------------
    # csv2xlsx
    # -----------------------
    p_csv2xlsx = subparsers.add_parser(
        "csv2xlsx", help="Преобразовать CSV → XLSX"
    )
    p_csv2xlsx.add_argument("--in", dest="input", required=True, help="Входной CSV-файл")
    p_csv2xlsx.add_argument("--out", dest="output", required=True, help="Выходной XLSX-файл")

    args = parser.parse_args()

    # -----------------------
    # Выполнение команд
    # -----------------------
    in_path = Path(args.input)
    out_path = Path(args.output)

    try:
        if args.command == "json2csv":
            json_to_csv(in_path, out_path)
            print(f"Готово: {in_path} → {out_path}")

        elif args.command == "csv2json":
            csv_to_json(in_path, out_path)
            print(f"Готово: {in_path} → {out_path}")

        elif args.command == "csv2xlsx":
            csv_to_xlsx(in_path, out_path)
            print(f"Готово: {in_path} → {out_path}")

    except FileNotFoundError:
        print(f"Ошибка: файл '{in_path}' не найден.", file=sys.stderr)
        sys.exit(1)

    except ValueError as e:
        print(f"Ошибка данных: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```

![Картинка 3](../../images/lab06/03.png)
![Картинка 4](../../images/lab06/04.png)
![Картинка 5](../../images/lab06/05.png)
