#task_1
arg_1 = int(input("Введите первое число:"))
arg_2 = int(input("Введите второе число:"))
def my_division ():
    return arg_1 / arg_2
if arg_2 == 0:
    print("На ноль делить нельзя")
else:
    print (my_division())

#task_2
your_name = input("Введите ваше имя:")
your_family = input("Введите вашу фамилию:")
your_birth = int(input("Введите год рождения:"))
your_city = input("Введите город проживания:")
your_email = input("Введите имэйл:")
your_phone_number = input("Введите номер телефона:")

def my_func(your_name, your_family, your_birth, your_city, your_email, your_phone_number):
    return ' '.join([your_name, your_family, your_birth, your_city, your_email, your_phone_number])
print(your_name, your_family, your_birth, your_city, your_email, your_phone_number)

#task_3
def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Result : {my_func(int(input("Введите первое число:")), int(input("Введите второе число:")), int(input("Введите третье число:")))}')




def my_func(arg_1, arg_2, arg_3):
    arguments = [arg_1, arg_2, arg_3]
    arguments.sort(reverse = True)
    return(arguments[0]+arguments[1])
print(f'Result : {my_func(int(input("Введите первое число:")), int(input("Введите второе число:")), int(input("Введите третье число:")))}')

#task_4

def exponenta (a, b):
    print(a ** b)
exponenta(int(input()), int(input()))

def exponenta (a, b):
    c = 1.0
    for _ in range(-b):
        c /= a
    print(c)
exponenta(int(input("Введите число:")), int(input("Введите степень:")))
#task_5

while 1:
    i = input("Введите числа:")
    i = i.split(" ")
    a = 0
    flag = False
    while a<len(i):
        try:
            i[a] = int(i[a])
        except ValueError:
            print("Value Error")
            flag = True
            break
        a = a + 1
    if flag:
        break
    z = 0
    for c in i:
        z = z + c
    print(z)



#task_5

def int_func (*args):
    word = input("Введите слова на латинице с маленькой буквы: ")
    print(word.title())
    return
int_func()
