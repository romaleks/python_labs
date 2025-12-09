import csv
from pathlib import Path

from src.lab08.models import Student


HEADER = ["fio", "birthdate", "group", "gpa"]


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("w", encoding="utf-8", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(HEADER)

    def _read_all(self) -> list[dict]:
        with open(self.path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
        if reader.fieldnames != HEADER:
            raise ValueError("Некорректный формат CSV: неверные заголовки")

        return rows

    def _write_all(self, rows: list[dict]):
        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=HEADER)
            writer.writeheader()
            writer.writerows(rows)

    # -------------------------
    # CRUD
    # -------------------------
        
    def list_(self) -> list[Student]:
        rows = self._read_all()
        return [Student(**r) for r in rows]

    def add(self, student: Student):
        rows = self._read_all()

        rows.append({
            "fio": student.fio,
            "birthdate": student.birthdate,
            "group": student.group,
            "gpa": str(student.gpa),
        })

        self._write_all(rows)

    def find(self, substr: str) -> list[Student]:
        rows = self._read_all()
        found = [r for r in rows if substr.lower() in r["fio"].lower()]
        return [Student(**r) for r in found]

    def remove(self, fio: str) -> bool:
        rows = self._read_all()
        new_rows = [r for r in rows if r["fio"] != fio]

        deleted = (len(new_rows) != len(rows))
        if deleted:
            self._write_all(new_rows)

        return deleted

    def update(self, fio: str, **fields):
        rows = self._read_all()
        updated = False

        for r in rows:
            if r["fio"] == fio:
                for key, value in fields.items():
                    if key not in HEADER:
                        raise ValueError(f"Поле {key} недопустимо")
                    r[key] = value
                updated = True
                break

        if not updated:
            raise ValueError(f"Студент {fio} не найден")

        self._write_all(rows)