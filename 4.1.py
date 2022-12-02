import random
import timeit

def qusort(a):
    if len(a)<=1:
        return a
    else:
        b=random.choice(a)
    left=[n for n in a if n<b]
    mid=[b]
    right=[n for n in a if n>b]
    return qusort(left)+mid+qusort(right)

def rasc(a):
    n = len(a)
    step = n

    while step > 1 or flag:
        if step > 1:
            step -= 1
        flag, i = False, 0
        while i + step < n:
            if a[i] > a[i + step]:
                a[i], a[i + step] = a[i + step], a[i]
                flag = True
            i += step
    return a

a=[random.randint(1,1000) for i in range(100)]
#s=input()
#if s=="quick":
print(a)
    #print(qusort(a))
print(timeit.timeit("rasc(a)", setup="from __main__ import rasc, a", number=1))
#elif s=="rasches":
#print(a)
#print(rasc(a))