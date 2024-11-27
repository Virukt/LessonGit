#TODO Задание 1
x = int(input())
y = int(input())

if x > 1 and y > 1:
    print('I')
if x == 1 and y == 1:
    print('II')
if x < 1 and y < 1:
    print('III')
if x > 2 and y > 2:
    print('IV')

#TODO Задание 2
def ask_password():
    count = 1
    pas = 'password'
    while count > 0:
        text = input('Введите пароль:')
        if text == pas:
              return'Пароль принят '
              break
        else:
              count -= 1
    else:
        return "В доступе отказанно!"
             
print(ask_password())