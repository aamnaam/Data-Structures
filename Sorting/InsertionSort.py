import random


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i

        # Swapping till element at 'i' initially reaches correct position
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    return arr


def insertion_less_swap(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key

    return arr


# O(n log(n)) comparisons (with help of binary search), O(n^2) swaps
def binary_insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i

        # Index that needs to be reached by number initially at 'i'
        desired_index = binary_search(arr, key, 0, i)

        while j > desired_index:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key

    return arr


def binary_search(arr, val, low, high):
    if low == high:
        if arr[low] > val:
            return low
        else:
            return low + 1

    mid = (low + high) // 2

    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, high)
    elif arr[mid] > val:
        return binary_search(arr, val, low, mid - 1)
    else:
        return mid


def main():
    arr = [5, 4, 3, 2, 1]
    random_list = random.sample(range(10), 5)
    print("Unsorted list: {}".format(arr))
    print("Random list: {}".format(random_list))
    # arr = random_list

    print(insertion_sort(arr))
    print(insertion_less_swap(arr))
    print(binary_insertion_sort(arr))


if __name__ == '__main__':
    main()
