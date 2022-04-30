a = [100, 100, 1, 3, 5, 6, 9]


# 返回 x 在 arr 中的索引，如果不存在返回 r
def binarySearch(arr, l, r, x):
    if r > l:
        mid = int(l + (r - l) / 2)

        # 元素整好的中间位置
        if arr[mid] >= x and arr[mid - 1] <= x:
            return mid

        # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        return r

def half_insert_sort(a):
    b = a[:]
    for i in range(1, len(a)):
        x = binarySearch(b, 0, i, a[i])
        print(i, x, ":", b)
        b.remove(a[i])
        b.insert(x, a[i])
    else:
        print("sorted a:", b)
    return b


b = half_insert_sort(a)
print("result", b)
