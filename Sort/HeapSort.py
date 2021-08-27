def heapInsert(arr, index):
    while arr[index] > arr[int((index - 1) / 2)]:  # 比较子节点的值是否大于父节点的值
        swap(arr, index, int((index - 1) / 2))  # 交换父子节点的位置
        index = int((index - 1) / 2)  # 将当前索引移动到父节点， 再继续判断上层的父子节点大小关系


def heapify(arr, index, heapSize):  # 某个数在index，判断是否可以往下移动
    left = index * 2 + 1  # 计算左子节点的索引值
    while left < heapSize:
        # 比较左右孩子谁的值大，把下标赋值给largest
        largest = left + 1 if left + 1 < heapSize and arr[left] < arr[left + 1] else left
        # 比较父节点与 孩子最大值 谁大,把下标给largest
        largest = largest if arr[largest] > arr[index] else index
        if largest == index:
            break
        swap(arr, largest, index)  # 交换值的位置当父节点的值小于子节点时，
        index = largest  # 往下移动索引位置至 子节点处
        left = index * 2 + 1  # 重新计算左子节点的索引


def heapSort(arr):
    if arr == None or len(arr) < 2:
        return
    for i in range(len(arr)):
        heapInsert(arr, i)

    heapSize = len(arr)-1
    swap(arr, 0, heapSize)
    while heapSize > 0:
        heapify(arr, 0, heapSize)
        heapSize -= 1
        swap(arr, 0, heapSize)




def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


if __name__ == '__main__':
    a = [1, 9, 6, 2, 3, 7, 8, 4, 5, 1, 9, 6, 2, 3, 7, 8, 4, 5, 10, 10]
    heapSort(a)
    print(a)
