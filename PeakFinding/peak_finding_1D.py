# Peak in a 1D list is an element that is NOT LESS THAN any of it's neighbours.
# For elements at the corners, the single neighbour is considered.
# This algorithm returns the index of peak of a given list of numbers (a peak always exists)
# Note that this may not be the global peak/maxima, only local
# Example: [1, 4, 8, 3, 9, 5]
# Naive --> 2, Recursive --> 2
# Example: [1, 19, 4, 2, 7, 10, 14, 13, 4]
# Naive --> 1, Recursive --> 6


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
    example_list = [1, 19, 4, 2, 7, 10, 14, 13, 4]
    n = len(example_list)

    print(example_list)
    print("Peak index using Naive algorithm =", naive_pf(example_list))
    print("Peak index using Recursive algorithm =", recursive_peak(example_list, 0, n - 1, n))


if __name__ == '__main__':
    main()


