# 10
# Ввести текст телеграммы. Найти стоимость телеграммы при тарифе 10 рублей за слово

print('Введите текст телеграммы:')

telegram_text = input()
word_cost = 10

def get_telegram_cost(text):
    telegram_cost = len(text.split()) * word_cost

    print(f'Стоимость телеграммы составит {telegram_cost} рублей')


get_telegram_cost(telegram_text)