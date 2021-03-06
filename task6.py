'''
6. Дана строка в виде случайной последовательности чисел от 0 до 9.
Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int),
а в качестве значений – количество этих чисел в имеющейся последовательности.
Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр.
Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.
'''
import random

def count_it(sequence):
    dict_ = {}
    #Можно ли нижеследующий цикл с условными операторами сделать в виде тернарного оператора для лаконичности?
    for i in str(sequence):
        if i in dict_:
            dict_[i] += 1
        else:
            dict_[i] = 1
    sorted_dict = {}
    sorted_keys = sorted(dict_, key=dict_.get, reverse=True)
    for w in sorted_keys[:3]:
        sorted_dict[w] = dict_[w]
    return sorted_dict

# Эта функция генерирует последовательность случайной длины от 15 до 50 чисел, состоящей из случайных чисел от 0 до 9
def gen_sequence():
    a = ""
    l = random.randint(15, 50)
    for i in range(l):
        a += str(random.randint(0,9))
    return int(a)

seq = gen_sequence()
print(seq)
print(count_it(seq))