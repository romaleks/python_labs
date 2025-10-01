def format_record(rec: tuple) -> str:
  """
    Форматирует запись студента в строку.
    
    Args:
        rec: Кортеж (fio: str, group: str, gpa: float)
    
    Returns:
        Строка формата: "Фамилия И.О., гр. GROUP, GPA X.XX"
    
    Raises:
        ValueError: Если ФИО или группа пустые, или GPA отрицательный
        TypeError: Если типы данных не соответствуют ожидаемым
  """
  if not isinstance(rec, tuple) or len(rec) != 3:
    raise TypeError("Запись должна быть кортежем из 3 элементов")
  
  fio, group, gpa = rec

  if not isinstance(fio, str):
    return TypeError("ФИО должно быть строкой")
  if not isinstance(group, str):
    return TypeError("Группа должна быть строкой")
  if not isinstance(gpa, (int, float)):
    return TypeError("GPA должно быть числом")
  
  # Проверка значений
  fio_clean = ' '.join(fio.split()).strip()
  if not fio_clean:
      raise ValueError("ФИО не может быть пустым")
  
  group_clean = group.strip()
  if not group_clean:
      raise ValueError("Группа не может быть пустой")
  
  if gpa < 0:
      raise ValueError("GPA не может быть отрицательным")
  
  # Обработка ФИО
  parts = fio_clean.split()
  surname = parts[0].lower()
  surname = surname[0].upper() + surname[1:]
  
  # Формирование инициалов
  initials = []
  for name_part in parts[1:]:
      if name_part:
          initials.append(f"{name_part[0].upper()}.")
  
  if not initials:
      formatted_fio = surname
  else:
      formatted_fio = f"{surname} {''.join(initials)}"
  
  # Форматирование GPA с 2 знаками после запятой
  formatted_gpa = f"{gpa:.2f}"
  
  return f"{formatted_fio}, гр. {group_clean}, GPA {formatted_gpa}"

test_cases = [
        ("Иванов Иван Иванович", "BIVT-25", 4.6),
        ("Петров Пётр", "IKBO-12", 5.0),
        ("Петров Пётр Петрович", "IKBO-12", 5.0),
        ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
    ]
    
for i, test_case in enumerate(test_cases, 1):
    result = format_record(test_case)
    print(f"Тест {i}: {result}")