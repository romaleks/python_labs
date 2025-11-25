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
    p_json2csv.add_argument(
        "--in", dest="input", required=True, help="Входной JSON-файл"
    )
    p_json2csv.add_argument(
        "--out", dest="output", required=True, help="Выходной CSV-файл"
    )

    # -----------------------
    # csv2json
    # -----------------------
    p_csv2json = subparsers.add_parser("csv2json", help="Преобразовать CSV → JSON")
    p_csv2json.add_argument(
        "--in", dest="input", required=True, help="Входной CSV-файл"
    )
    p_csv2json.add_argument(
        "--out", dest="output", required=True, help="Выходной JSON-файл"
    )

    # -----------------------
    # csv2xlsx
    # -----------------------
    p_csv2xlsx = subparsers.add_parser("csv2xlsx", help="Преобразовать CSV → XLSX")
    p_csv2xlsx.add_argument(
        "--in", dest="input", required=True, help="Входной CSV-файл"
    )
    p_csv2xlsx.add_argument(
        "--out", dest="output", required=True, help="Выходной XLSX-файл"
    )

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
