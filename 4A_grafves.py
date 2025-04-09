import timeit

def count_vertices(edges):
    """Подсчет количества вершин в графе."""
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return len(vertices)

def get_vertices(edges):
    """Получение списка вершин из списка ребер."""
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return list(vertices)




# Пример использования
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 6), (6, 7), (7, 5)]
vertices = get_vertices(edges)
my_dict = {'1': 777,'2': 666,'3': 555,'4': 444,'5': 333,'6': 222,'7': 111}

#n = len(my_dict)
#for i in range(n):
#    for j in range(0,n - i - 1):
#        if my_dict[j] > my_dict[j+1]:
#            fff = my_dict[1]
#            my_dict[1] = my_dict[2]
#            my_dict[2] = fff
#print(my_dict)
start = timeit.default_timer()
print("The start time is :",start)
n = len(my_dict)
spis = list(my_dict.items())
for i in range(n):
    for j in range(0,n-i-1):
        if spis[j][1] > spis[j+1][1]:
            spis[j], spis[j + 1] = spis[j+1], spis[j]
print("The difference of time is :", timeit.default_timer() - start)
print(spis)

### for i in my_dict: ключи



value = int(input())

    

# индексы первого элемента, последнего и среднего
low = 0
high = len(spis) - 1
mid = len(spis) // 2
    

while spis[mid][1] != value and low <= high:
    if value > spis[mid][1]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2
        

if low > high:
    print('no element')
else:
    print("id:",spis[mid][0])




#https://timeweb.cloud/tutorials/python/kak-preobrazovat-spisok-v-slovar-python
#https://www.geeksforgeeks.org/iterate-over-a-dictionary-in-python/
#https://translated.turbopages.org/proxy_u/en-ru.ru.9e4b62ca-67f64198-a673d1c6-74722d776562/https/www.geeksforgeeks.org/python-remove-last-element-from-dictionary/