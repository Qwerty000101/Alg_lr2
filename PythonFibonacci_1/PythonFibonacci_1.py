import timeit
import matplotlib.pyplot as plt
def FibRecursive(n):
    if n<=1:
        return n
    else:
        return FibRecursive(n-1)+FibRecursive(n-2)
def FibArray(n):
    F=[0 for i in range(0,n+1)]
    F[0],F[1]=0,1
    for i in range(2,n+1):
        F[i]=F[i-1]+F[i-2]
    return F[n]
time_fib_recursive =(timeit.timeit(lambda: FibRecursive(10), number=100000))/100000
time_fib_array = (timeit.timeit(lambda: FibArray(10), number=100000))/100000
FR=FibRecursive(10)
FA=FibArray(10)
print("FibRecursive(10) =", FR, ",время выполнения:", time_fib_recursive)
print("FibArray(10) =",FA, ",время выполнения:", time_fib_array)
if time_fib_recursive < time_fib_array:
    print("Функция FibRecursive быстрее")
else:
    print("Функция FibArray быстрее")
x=[1,2,3,4,5,6,7,8,9,10]
y1=[]
y2=[]
c=10000
for i in range(1,11):
    time_fib_recursive = timeit.timeit(lambda: FibRecursive(i), number=c)
    time_fib_array = timeit.timeit(lambda: FibArray(i), number=c)
    y1.append(time_fib_recursive/c)
    y2.append(time_fib_array/c)
plt.figure(1)
plt.plot(x, y1, "--",x,y2,"-")
plt.legend(['FibRecursive(n)', 'FibArray(n)'])
plt.xlabel("Значение n")
plt.ylabel("Время выполнения")
plt.show()