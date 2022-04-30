a = [7, 8, 1, 3, 5, 6]

def bubble_sort(a):
    target = len(a) - 1
    while target > 0:
        for i in range(target):
            if i + 1 > len(a) - 1:
                break
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        print(target, a)
        target -= 1
    return a

b = bubble_sort(a)
print("sorted a:", b)
