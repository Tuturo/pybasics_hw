# 9
# Ввести текст. Капитализировать (первая буква прописная остальные строчные) каждое слово этого текста
# "Привет всем слуШатлеям" - > "Привет Всем Слушателям"

import string

print('Введите текст:')

new_text = input()

def get_capitalize_words(text):
    current_list = text.split()
    
    for i in range(len(current_list)):
        current_list[i] = current_list[i].capitalize()
    
    print(' '.join(current_list))


get_capitalize_words(new_text)