a = [1, 2, 3, 6, 8, 9]
x = 8

# build fibonacci list.
n = len(a)
fp, f = 0, 1
fibonacci = [fp, f]
while True:
    f, fp = f+fp, f
    if f > n:
        break
    fibonacci.append(f)

print(fibonacci)

def fibonacci_search(arr, fi, i, x):
    if i >= 0:
        mid = i
        print(fi, i)
        # 元素整好的中间位置
        if arr[mid] == x:
            return mid

        # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:

            i -= fibonacci[fi - 1]
            return fibonacci_search(arr, fi - 1, i, x)

        # 元素大于中间位置的元素，只需要再比较右边的元素
        else:

            i += fibonacci[fi - 1]
            return fibonacci_search(arr, fi - 1, i, x)

    else:
        return len(arr)

if __name__=="__main__":
    position = fibonacci_search(a, len(fibonacci)-1,fibonacci[len(fibonacci)-1], x)
    print("x found in array a:", position)