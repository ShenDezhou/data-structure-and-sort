a = [100, 100, 1, 2, 4, 5, 9]

def insert_sort(a):
    b = a[:]
    for i in range(1, len(a)):
        for j in range(i):
            print(i, j, ":", b)
            if b[j] < a[i]:
                continue
            else:
                # found the index j, insert element i at the position j.
                b.remove(a[i])
                b.insert(j, a[i])
                break
    else:
        print("sorted a:", b)
    return b


b = insert_sort(a)
print("result", b)

