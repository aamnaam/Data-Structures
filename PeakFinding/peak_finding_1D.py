# O(n), naive search through all elements
def naive_pf(arr):
    n = len(arr)

    if n == 1:
        return 0

    if arr[0] >= arr[1]:
        return 0

    if arr[n - 1] >= arr[n - 2]:
        return n - 1

    for index in range(1, n - 1):
        if arr[index] == max(arr[index], arr[index - 1], arr[index + 1]):
            return index


# O(log(n)),
def recursive_peak(arr, low, high, n):
    mid = int(low + (high - low) / 2)

    # if element left to mid is greater than element at mid, there is always a peak in left half of view
    if arr[mid] < arr[mid - 1]:
        return recursive_peak(arr, low, mid - 1, n)

    # if element right to mid is greater than element at mid, there is always a peak in right half of view
    elif arr[mid] < arr[mid + 1]:
        return recursive_peak(arr, mid + 1, high, n)

    # since element at mid is NOT LESS than any neighbouring elements, it is a peak
    else:
        return mid


# List must not have adjacent equal elements
def main():
    example_list = [2, 5, 7, 8, 16, 13, 11, 10, 9]
    n = len(example_list)

    print(example_list)
    print("Peak index =", recursive_peak(example_list, 0, n - 1, n))


if __name__ == '__main__':
    main()


