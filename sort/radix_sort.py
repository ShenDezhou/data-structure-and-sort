a = [11, 3, 5, 7, 2, 6]

def radix_sort(a):
    la = [len(str(i)) for i in a]
    n = max(la)
    b = a
    for i in range(n):
        radix_heaps = [[] for i in range(10)]
        for x in b:
            heap_i = (x >> i) % 10
            radix_heaps[heap_i].append(x)
        c = []
        for h in radix_heaps:
            c.extend(h)
        b = c
    return b

b = radix_sort(a)
print("sorted a:", b)