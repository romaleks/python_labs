import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import normalize, tokenize, count_freq, top_n

# Чтение всего ввода из stdin
text = sys.stdin.readline()

# Нормализация текста
normalized_text = normalize(text)

# Токенизация
tokens = tokenize(normalized_text)

# Подсчет статистики
total_words = len(tokens)
freq_dict = count_freq(tokens)
unique_words = len(freq_dict)
top_words = top_n(freq_dict, 5)

# Вывод результатов
print(f"Всего слов: {total_words}")
print(f"Уникальных слов: {unique_words}")
print("Топ-5:")

for word, count in top_words:
    print(f"{word}:{count}")