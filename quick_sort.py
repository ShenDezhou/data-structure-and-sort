a = [8, 3, 4, 7, 9, 1]


def quick_sort(a, l, r):
    if r - l == 0:
        return
    i, j = l, r
    key = a[l]
    pivot = -1
    while i < j:
        while a[j] > key:
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]

        while a[i] < key:
            i += 1
        else:
            a[i], a[j] = a[j], a[i]
    else:
        pivot = i
        print("pivot:", pivot)
        print(l, r, ":", a)
    if pivot - 1 > l:
        quick_sort(a, l, pivot - 1)
    if r > pivot + 1:
        quick_sort(a, pivot + 1, r)
    return a


b = quick_sort(a, 0, len(a) - 1)
print("sorted a:", b)
