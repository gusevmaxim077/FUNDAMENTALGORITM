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
my_dict = {1: 777,2: 666,3: 555,4: 444,5: 333,6: 222,7: 111}

#n = len(my_dict)
#for i in range(n):
#    for j in range(0,n - i - 1):
#        if my_dict[j] > my_dict[j+1]:
#            fff = my_dict[1]
#            my_dict[1] = my_dict[2]
#            my_dict[2] = fff
#print(my_dict)

my_dictred = my_dict
for i in my_dict:
    my_dictred = my_dictred.popitem()
    for j in my_dictred:
        if my_dictred[j] > my_dictred[j+1]



#https://timeweb.cloud/tutorials/python/kak-preobrazovat-spisok-v-slovar-python
#https://www.geeksforgeeks.org/iterate-over-a-dictionary-in-python/
#https://translated.turbopages.org/proxy_u/en-ru.ru.9e4b62ca-67f64198-a673d1c6-74722d776562/https/www.geeksforgeeks.org/python-remove-last-element-from-dictionary/