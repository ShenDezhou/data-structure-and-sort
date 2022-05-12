a = "23901029303485649399232322"
b = "232322"


def knuth_morris_pratt_search(a, b):
    nb = len(b)
    # pattern b's path: the maximum prefix.
    path_b = [0] * nb
    k = 0
    for i in range(1, nb):
        while k > 0 and b[k] != b[i]:
            k = path_b[k]
        if b[k] == b[i]:
            k += 1
        path_b[i] = k
    print(path_b)

    q = 0
    for i in range(len(a)):
        while q > 0 and b[q] != a[i]:
            q = path_b[q]
        if b[q] == a[i]:
            q += 1
        if q == nb:
            return i - q + 1
    return -1

position = knuth_morris_pratt_search(a, b)
print("Pattern b index in string a is:", position)