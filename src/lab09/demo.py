from .group import Group
from ..lab08.models import Student


group = Group("data/lab09/students.csv")
student = Student(
    fio="Сергеев Сергей",
    birthdate="2003-05-27",
    group="БИВТ-21-2",
    gpa="2.1",
)

print(group.list_())
group.add(student)
print(group.list_())
print(group.find("Петров"))
group.remove("Иванов Иван")
print(group.list_())
group.update("Сергеев Сергей", gpa="2.6")
print(group.list_())