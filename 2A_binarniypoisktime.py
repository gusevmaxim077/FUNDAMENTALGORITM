import timeit
import random
from random import randint

    
def fun():
    kol_vo = 0
    # индексы первого элемента, последнего и среднего
    low = 0
    high = len(a) - 1
    mid = len(a) // 2
    

    while a[mid] != value and low <= high:
        kol_vo += 1
        if value > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
        

    if low > high:
        return('no element',"kol-vo:",kol_vo)
    else:
        return("id:",mid,"kol-vo:",kol_vo)


    # создание списка, его сортировка по возрастанию и вывод на экран
for j in range(10):
    a = []
    for i in range(10000):
        a.append(randint(1, 50000))
    a.sort()
    print(a)
    # искомое число
    value = randint(1, 50)