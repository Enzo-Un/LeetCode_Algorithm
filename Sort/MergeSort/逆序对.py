def nixudui(arr, L, R):
    if arr == None or len(arr) < 2:
        return 0
    return process(arr, 0, len(arr) - 1)


def process(arr, L, R):
    if L == R:return
    mid = L + ((R - L) >> 1)
    process(arr, L, mid)
    process(arr, mid + 1, R)
    merge(arr, L, mid, R)


def merge(arr, L, M, R):
    help = [None for i in range(R - L + 1)]
    i = 0
    p1 = L
    p2 = M + 1
    while p1 <= M and p2 <= R:
        if arr[p1] > arr[p2]:
            print(arr[p1], arr[p2])
        if arr[p1] < arr[p2]:
            help[i] = arr[p1]
            p1 += 1
        else:
            help[i] = arr[p2]  # 如果两者相等，一定先将右组的元素拿出来，因为左组元素依然需要和右组剩余的元素进行比较
            p2 += 1
        i += 1

    while p1 <= M:
        help[i] = arr[p1]
        i += 1
        p1 += 1
    while p2 <= R:
        help[i] = arr[p2]
        i += 1
        p2 += 1

    j = 0
    while j < len(help):
        arr[L + j] = help[j]
        j += 1



if __name__ == '__main__':
    a = [1, 2, 3, 7, 8, 4, 5, 10]
    L = 0
    R = len(a) - 1
    small_sum = nixudui(a, L, R)
    print(a)
