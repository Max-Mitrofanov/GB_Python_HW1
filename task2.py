# Пользователь вводит время в секундах. 
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. 
# Используйте форматирование строк.

print('Введите время в секундах чтобы получить чч:мм:сс :')
user_time = int(input())

def calc_time (seconds):
    hours = seconds // 3600
    minutes = seconds % 3600 // 60
    sec = seconds % 3600 % 60
    print(f'{hours:02}:{minutes:02}:{round(sec, 2):02}')

calc_time(user_time)



