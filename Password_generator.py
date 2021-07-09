# Генератор безопасных паролей
import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

num = int(input('Сколько нужно паролей?: '))
len_n = int(input('Какая должна быть длина пароля?: '))
num_in = input('Включаем ли в пароль цифры? Введите "да" или "нет": ').lower()
let_low = input('Включаем ли в пароль прописные буквы? Введите "да" или "нет": ').lower()
let_upp = input('Включаем ли в пароль заглавные буквы? Введите "да" или "нет": ').lower()
symb = input('Включаем ли в пароль символы? Введите "да" или "нет": ').lower()
symb_n = input('Исключаем ли неоднозначные символы "il1Lo0O"? Введите "да" или "нет": ').lower()

for _ in range(num):
    if num_in == 'да':
        chars += digits
    if let_low == 'да':
        chars += lowercase_letters
    if let_upp == 'да':
        chars += uppercase_letters
    if symb == 'да':
        chars += punctuation
    if symb_n == 'да':
        for i in 'il1Lo0O':
            chars = chars.replace(i, '')
    password = ''
    for _ in range(len_n):
        password += random.choice(chars)
    print('Безопасный пароль: ', password)