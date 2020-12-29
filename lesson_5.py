# task_1
with open("task_1.txt", "w") as file:
    while True:
        strings = input("Введите текст:")
        if strings == "":
            break
        file.write(strings)
# task_2
f = open('task_2.txt', encoding='utf-8')
line = 0
for i in f:
    line += 1

    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(i, len(i), 'симв.', word, 'сл.')

print(line, 'стр.')
f.close()
# task_3
summa = 0
count = 0
persons = []
with open("task_3.txt", "r", encoding='utf-8') as file_obj:
    for line in file_obj:
        tokens = line.split(' ')
        if len(tokens) < 2:
            continue
        if int(tokens[1]) <= 20000:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"persons: {persons}")
print(f"average: {result}")
# task_4
translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []
result = []
try:
    file_obj = open("task_4.txt", 'r', encoding='utf-8')
    for line in file_obj:
        tokens = line.split(" - ")
        print(tokens)
        if tokens[0] in translator:
            word = translator[tokens[0]]
            result.append(word + ' - ' + tokens[1])
    print(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()

try:
    file_input = open("task_4.txt", "w", encoding='utf-8')
    file_input.writelines(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_input.close()


# task5
def summary():
    try:
        with open('task_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел: \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')


summary()

# task_6
FILENAME = "task_6.txt"

subjects = {}

try:
    with open(FILENAME, encoding='utf-8') as fh:
        lines = fh.readlines()

    for line in lines:
        data = line.replace('(', ' ').split()

        subjects[data[0][:-1]] = sum(
            int(i) for i in data if i.isdigit()
        )
except IOError as e:
    print(e)
except ValueError:
    print("Неверные данные")

print(subjects)

# task_7
import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('task_7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль- отсутствует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')
