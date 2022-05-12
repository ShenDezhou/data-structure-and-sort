a = [2, 3, 4, 6, 8, 9]
x = 9

# 返回 x 在 arr 中的索引，如果不存在返回 r
def binary_search(arr, l, r, x):
    if r > l:
        mid = int(l + (r - l) / 2)

        # 元素整好的中间位置
        if arr[mid] == x:
            return mid

        # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)

        # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binary_search(arr, mid + 1, r, x)

    else:
        return r

if __name__ == "__main__":
    position = binary_search(a, 0, len(a), x)
    print("x found in array a:", position)
