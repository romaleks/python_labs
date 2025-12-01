from .serialize import students_from_json

students = students_from_json("data/lab08/students_input.json")
for student in students:
    print(student)