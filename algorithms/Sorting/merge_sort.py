def merge_sort(array):
    if len(array) > 1:

        M = len(array) // 2
        L = array[:M]
        R = array[M:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Until we reach either end of either L or R, pick larger among
        # elements L and R and place them in the correct position at A[p..M]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        # When we run out of elements in either L or R,
        # pick up the remaining elements and put in A[p..M]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1


def print_list(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


if __name__ == '__main__':
    array = [5, 2, 7, 6, 3, 1, 9, 4, 8]
    merge_sort(array)
    print("Sorted: ", end='')
    print_list(array)