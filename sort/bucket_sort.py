import sys
sys.path.append("../data_structure")
# use the data_structure Node and Link
from link import Node, Link
from insert_sort import insert_sort

a = [4, 2, 1, 8, 9]


def normalize(a, __min, __max):
    b = [float(i - __min) / (__max - __min) for i in a]
    return b

def denormalize(a, __min, __max):
    b = [i * (__max - __min) + __min for i in a]
    return b

def lookup(x, step):
    if x < 0 or x >= 1:
        return -1
    index = int(x // step)
    return index

def bucket_sort(a):
    za = min(a)
    zz = max(a)
    na = normalize(a, za, zz)
    n = len(a)
    step = float(zz - za) / zz / n
    # build bucket link
    buckets = [Node(step * i) for i in range(n)]
    # find the bucket position for each element of a.
    bp = [lookup(i, step) for i in na]
    # bucket insertion
    for i in range(n):
        na_i = na[i]
        bp_i = bp[i]
        bucket = buckets[bp_i] # This is a Node.
        # bucket.pointer is a Link/List.
        if bucket.pointer is None:
            bucket.pointer = []
        bucket.pointer.append(na_i)

    # sort each bucket.
    for bucket in buckets:
        if bucket.pointer:
            bucket.pointer = insert_sort(bucket.pointer)

    c = []
    for bucket in buckets:
        if bucket.pointer:
            t = insert_sort(bucket.pointer)
            c.extend(t)

    d = denormalize(c, za, zz)
    # type convertion
    d = [int(i) for i in d]
    return d

b = bucket_sort(a)
print("sorted a:", b)




