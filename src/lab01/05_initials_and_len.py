fio = input('ФИО: ')
names = fio.split()
print(f'Инициалы: {names[0][0]}{names[1][0]}{names[2][0]}.')
print(f'Длина (символов): {sum(len(name) for name in names) + 2}')