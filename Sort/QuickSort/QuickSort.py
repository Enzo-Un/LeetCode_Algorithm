import random


def quickSort(arr, L, R):
    if L < R:
        swap(arr, int(L + random.random() * (R - L + 1)), R)
        left_bound, right_bound = partition(arr, L, R)  # 通过partition获得等于区域的左边界右边界
        # 将小于区域也做quickSort，
        quickSort(arr, L, left_bound - 1)
        # 将大于区域也做quickSort
        quickSort(arr, right_bound + 1, R)


def partition(List, L, R): # 划分函数
    less = L - 1  # 小于区 右边界
    more = R  # 大于区 左边界
    while L < more:
        if List[L] < List[R]:
            less += 1
            swap(List, less, L)
            L += 1
        elif List[L] > List[R]:
            more -= 1
            swap(List, more, L)
        else:
            L += 1

    swap(List, more, R)
    return less + 1, more # 返回等于区域的左边界和右边界

def swap(List, i, j):
    temp = List[i]
    List[i] = List[j]
    List[j] = temp


if __name__ == '__main__':
    a = [1, 9, 6, 2, 3, 7, 8, 4, 5, 1, 9, 6, 2, 3, 7, 8, 4, 5, 10, 10]
    L = 0
    R = len(a) - 1
    quickSort(a, L, R)
    print(a)
