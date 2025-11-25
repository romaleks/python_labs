price = int(input("Price (₽): "))
discount = int(input("Discount (%): "))
vat = int(input("Vat (%): "))
base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount
print(f"База после скидки: {format(base, '.2f')} ₽")
print(f"НДС: {format(vat_amount, '.2f')} ₽")
print(f"Итого к оплате: {format(total, '.2f')} ₽")
