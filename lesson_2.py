#task_1
my_integer = 10
my_string = "My string"
my_list = ["a" , "b" , "c" , "1" , "2" , "3"]
my_tuple = ("e", "f" , "g" , "4" , "5" , "6")
my_dict = {'letter': 'a', 'integer': '1'}

all_list = [my_integer, my_string, my_list, my_tuple, my_dict]
for q in all_list:
    print(f'{q} is {type(q)}')
#task_2
all_elements = int(input("Введите количество элементов списка: "))
my_list = []
i = 0
el = 0
while i < all_elements:
    my_list.append(input("Введите следующее значение списка: "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)
#task_3
month = int(input("Введите месяц числом:"))
seasons = {'winter':[12,1,2], 'spring':[3,4,5],  'summer': [6,7,8], 'fall':[9, 10, 11]}
for key, months in seasons.items():
 if month in months:
    print(key)
    break
else:
 print('no such month')


#task_4
new_string = str(input("Введите строку из нескольких слов:"))
my_word = []
num = 1
for el in range(new_string.count(' ') + 1):
    my_word = new_string.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [el]}")
        num += 1
    else:
        print(f" {num} {my_word [el] [0:10]}")
        num += 1

#task_5

your_rating = int(input("Введите ваш рейтинг:"))
all_rating = [8, 6, 5, 2]
all_rating.append(your_rating)
all_rating.sort(reverse = True)
print(all_rating)

#task_6
tuple_macbook = (1, {"название": "компьютер", "цена": 100000, "количество": 5, "eд": "шт."})
tuple_phone = (2, {"название": "телефон", "цена": 80000, "количество": 5, "eд": "шт."})
tuple_airpods = (3, {"название": "наушники", "цена": 20000, "количество": 4, "eд": "шт."})
tuple_ipad = (4, {"название": "планшет", "цена": 30000, "количество": 2, "eд": "шт."})

goods = int(input("Введите  количество всех товаров: "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    my_dict = dict({'название': input("введите наименование товара "), 'цена': input("Введите цену "),
                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
my_analys = {}
for i, my_dict in my_list:
   for key, val in my_dict.items():
      lst = my_analys.get(key, [])
      lst.append(val)
      my_analys[key] = lst
print(my_analys)
