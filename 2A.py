import timeit
import random
from random import randint



    # создание списка, его сортировка по возрастанию и вывод на экран
a = []
for i in range(10):
    a.append(randint(1, 50))
a.sort()
print(a)
# искомое число
value = int(input())

    
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

start = timeit.default_timer()
print("The start time is :",start)
a = fun()
print("The difference of time is :", timeit.default_timer() - start)
print(a)
