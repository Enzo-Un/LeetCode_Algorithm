def mergeSort(List, L, R):
    if L == R: return
    mid = L + ((R - L) >> 1)
    mergeSort(List, L, mid)
    mergeSort(List, mid + 1, R)
    merge(List, L, mid, R)
    return List

def merge(List, L, M, R):
    help = [None for i in range(R - L + 1)]
    i = 0
    p1 = L
    p2 = M + 1
    while p1 <= M and p2 <= R:
        if List[p1] <= List[p2]:
            help[i] = List[p1]
            p1 += 1
        else:
            help[i] = List[p2]
            p2 += 1
        i += 1
    while p1 <= M:
        help[i] = List[p1]
        i += 1
        p1 += 1
    while p2 <= R:
        help[i] = List[p2]
        i += 1
        p2 += 1
    j = 0
    while j < len(help):
        List[L + j] = help[j]
        j += 1


if __name__ == '__main__':
    a = [1, 9, 6, 2, 3, 7, 8, 4, 5,1, 9, 6, 2, 3, 7, 8, 4, 5,10,10]

    L = 0
    R = len(a) - 1
    sorted_a = mergeSort(a, L, R)
    print(sorted_a)
