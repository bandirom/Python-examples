
"""
https://all-python.ru/osnovy/itertools.html
Название	Назначение
count	Итерация с заданным шагом без ограничений
cycle	Итерация с повторением без ограничений
repeat	Итерация с повторением заданное количество раз
combinations	Комбинация всех возможных значений без повторяющихся элементов
combinations_with_replacement	Комбинация всех возможных значений с повторяющимися элементами
permutations	Комбинация с перестановкой всех возможных значений
product	Комбинация, полученная из всех возможных значений вложенных списков
filterfalse	Все элементы, для которых функция возвращает ложь
dropwhile	Все элементы, начиная с того, для которого функция вернет ложь
takewhile	Все элементы, до тех пор, пока функция не вернет истину
compress	Удаление элементов, для которых было передано значение ложь
chain	Поочередное объединение списков при помощи итераторов
chain.from_terable	Аналогично chain, но аргумент – список, в который вложены объединяемые списки.
islice	Получение среза, благодаря указанному количеству элементов
zip_longest	Объединение нескольких итераций с повышением размера до максимального
tee	Создание кортежа из нескольких готовых итераторов
groupby	Группировка элементов последовательности по некоторым ключевым значениям
accumulate	Каждый элемент результирующей последовательности равен сумме текущего и всех предыдущих исходной последовательности
starmap	В заданную функцию передает список подставляемых аргументов
"""
from itertools import count, cycle,\
    repeat, combinations,\
    combinations_with_replacement,\
    permutations, product

from itertools import filterfalse, dropwhile,\
    takewhile, \
    compress

from itertools import chain, starmap,\
    accumulate, islice, tee, groupby, zip_longest

for i in count(1, 3):
    if i >= 10:
        break
    else:
        print(i)

print('##########')

count = 1
for i in cycle('cycle'):
    if count > 6:
        break
    print(i)
    count += 1


data = [i for i in repeat('DOG', 3)]
print('repeat:', data)

data = list(combinations('DOG', 2))
print('combinations:', data)

data = [''.join(i) for i in combinations_with_replacement('DOG', 3)]
print('combinations_with_replacement:', data)

data = [''.join(i) for i in permutations('DOG', 3)]
print('permutations:', data)

data = list(product((0, 1), (2,3)))
print('product:', data)

temp = [1, 2, 3, 0, 4, 5, 1]

data = list(filterfalse(lambda i: i == 0, temp))
print('filterfalse:', data)

data = list(dropwhile(lambda i: i != 0, temp))
print('dropwhile:', data)

data = list(takewhile(lambda i: i != 0, temp))
print('takewhile', data)

data = list(compress('DOG', [True, False, True]))
print('compress', data)

data1 = ['D', 'O', 'G']
data2 = [0, 1, 2, 3, 4]
data = list(chain(data1, data2))
print('chain:', data)

data = [['D', 'O', 'G'], [0, 1, 2, 3, 4]]
data2 = [0, 1, 2, 3, 4]
data = list(chain.from_iterable(data))
print('chain.from_iterable:', data)

data = [i for i in starmap(pow, [(1, 2), (2, 2), (3, 2)])]
print('starmap + pow:', data)

data = list(accumulate([1, 2, 3, 4]))
print('accumulate:', data)

# data = [i for i in islice(count(0, 2), 5)]
# print('islice:', data)

# for i in islice(count(0, 2), 5):
#     print(i)

data = [i for i in zip_longest('DOG', [0, 1, 2, 3], fillvalue='')]
print('zip_longest:', data)

data = 'DOG'
i1, i2 = tee(data)
list1 = [i for i in i1]
list2 = [i for i in i2]
print('tee:', list1, list2)

animals = [('CAT', 'TOM'), ('MOUSE', 'JARRY')]
for key, group in groupby(animals, lambda kind: kind[0]):
    for kind, name in group:
        print('{name} is a {kind}'.format(name = name, kind = kind))

