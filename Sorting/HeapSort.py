def swap_param(L, i, j):
    L[i], L[j] = L[j], L[i]
    return L

# 重建堆，在当前结点交换完之后，检查交换后的子节点是否符合最大堆的条件
def heap_adjust(L, start, end):
    temp = L[start]

    i = start
    j = 2 * i

    while j <= end:
        if (j < end) and (L[j] < L[j + 1]):
            j += 1
        if temp < L[j]:
            L[i] = L[j]
            i = j
            j = 2 * i
        else:
            break
    L[i] = temp


def heap_sort(L):
    L_length = len(L) - 1

    first_sort_count = int(L_length / 2)
    # 构造最大堆
    for i in range(first_sort_count):
        heap_adjust(L, first_sort_count - i, L_length)

    for i in range(L_length - 1):
        L = swap_param(L, 1, L_length - i)
        # 重建剩余的数组组成最大堆
        heap_adjust(L, 1, L_length - i - 1)

    return [L[i] for i in range(1, len(L))]


L = [0, 90, 80, 50, 70, 60, 30, 2, 10, 16]
print(heap_sort(L))