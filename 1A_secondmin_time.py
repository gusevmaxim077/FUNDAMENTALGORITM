import timeit
import time


start = timeit.default_timer()
print("The start time is :", start)


time.sleep(20)
arr = [1,1,1,1,2]
min = arr[0]
min_old = min
for x in arr:
    if min > x:
         min_old = min
         min=x
    else:
        if min_old == min or x < min_old:
            min_old = x


print(min_old)


print("The difference of time is :", timeit.default_timer() - start)

# время исполнения = 0.0084 секунд
