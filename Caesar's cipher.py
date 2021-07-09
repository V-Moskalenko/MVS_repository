# Шифр Цезаря
alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_EUm = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
alfavit_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alfavit_RUm = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
shag = int(input('Шаг шифровки: '))

message = input("Сообщение для ДЕшифровки: ")

itog = ''
lang = input('Выберите язык RU/EU: ').upper()
if lang == 'RU':
    for i in message:
        mesto = alfavit_RU.find(i)
        mesto_m = alfavit_RUm.find(i)
        new_mesto = mesto + shag
        new_mesto_m = mesto_m + shag
        if i in alfavit_RU:
            itog += alfavit_RU[new_mesto]
        if i in alfavit_RUm:
            itog += alfavit_RUm[new_mesto_m]
        if i not in alfavit_RU and i not in alfavit_RUm:
            itog += i

if lang == 'EU':
    for i in message:
        mesto = alfavit_EU.find(i)
        mesto_m = alfavit_EUm.find(i)
        new_mesto = mesto + shag
        new_mesto_m = mesto_m + shag
        if i in alfavit_EU:
            itog += alfavit_EU[new_mesto]
        if i in alfavit_EUm:
            itog += alfavit_EUm[new_mesto_m]
        if i not in alfavit_EU and i not in alfavit_EUm:
            itog += i

print (itog)