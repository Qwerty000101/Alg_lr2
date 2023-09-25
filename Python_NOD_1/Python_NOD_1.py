import timeit
import matplotlib.pyplot as plt
def EuclidGCD(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a>=b:
        return EuclidGCD(a % b,b)
    if b>=a:
        return EuclidGCD(a,b%a)
def GCD(a,b):
    gcd=1
    for d in range(2,max(a,b)):
        if a%d==0 and b%d==0:
            gcd=d
    return gcd
time_gcd=(timeit.timeit(lambda: GCD(3918848,1653264), number=10))/10
time_euclid_gcd=(timeit.timeit(lambda: EuclidGCD(3918848,1653264), number=10))/10
gcd=GCD(3918848,1653264)
euclidGCD=EuclidGCD(3918848,1653264)
print("GCD(3918848,1653264) =", gcd, ",время выполнения:", time_gcd)
print("EuclidGCD(3918848,1653264) =",euclidGCD, ",время выполнения:", time_euclid_gcd)
if time_gcd > time_euclid_gcd:
    print("Функция EuclidGCD быстрее, чем GCD")
else:
    print("Функция GCD быстрее, чем EuclidGCD")
x2=[]
y1n=[]
y2n=[]
for i in range(1200000,1400000,83129):
    time_gcd = timeit.timeit(lambda: GCD(i,1320300), number=20)
    time_euclid_gcd = timeit.timeit(lambda: EuclidGCD(i,1320300), number=20)
    x2.append(i)
    y1n.append(time_gcd/20)
    y2n.append(time_euclid_gcd/20)
plt.figure(1)
plt.plot(x2, y1n, "--",x2,y2n,"-")
plt.legend(['GCD(a,b)', 'Euclid_GCD(a,b)'])
plt.xlabel("Значение a")
plt.ylabel("Время выполнения")
plt.show()