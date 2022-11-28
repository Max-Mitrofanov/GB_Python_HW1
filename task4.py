# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. 
# Для решения используйте цикл while и арифметические операции (а нахрена??)

print('Введите любое число')

user_number = input()
max_number = user_number[0]

for element in user_number:
    if element > max_number:
        max_number = element

print(max_number)