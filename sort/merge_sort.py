a = [3, 2, 1, 5, 9, 8, 7]

def merge_sort(a, b):
    if not isinstance(a, list) and not isinstance(b, list):
        if a < b:
            return [a, b]
        else:
            return [b, a]
    if not isinstance(a, list):
        a = [a]
    if not isinstance(b, list):
        b = [b]
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    else:
        if i < len(a):
            c.extend(a[i:])
        if j < len(b):
            c.extend(b[j:])
    return c


def merge_sort_algorithm(a):
    x = a
    while True:
        y = []
        for i in range(len(x) // 2):
            y.append(merge_sort(x[2*i], x[2*i+1]))
        else:
            if len(x) % 2 > 0:
                y.append([x[-1]])
        if len(y) == 1:
            return y[0]
        x = y
        print(y)

b = merge_sort_algorithm(a)
print(a)
print("sorted a:", b)
