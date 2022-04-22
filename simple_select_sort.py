a = [1, 5, 2, 4, 9, 8]

def simple_select_sort(a):
    target = len(a) - 1
    while target > 0:
        x = target
        for i in range(target):
            if a[i] > a[x]:
                x = i
        a[target], a[x] = a[x], a[target]
        target -= 1
        print(target, a)
    return a

b = simple_select_sort(a)
print('sorted a:', b)