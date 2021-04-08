import random


def merge_sort(arr):
    n = len(arr)

    if n > 1:
        # Creating left and right halves
        mid = n // 2
        l_arr = arr[:mid]
        r_arr = arr[mid:]

        # Sorting each half
        l_arr_sorted = merge_sort(l_arr)
        r_arr_sorted = merge_sort(r_arr)

        # Sort-merge of both halves gives complete sorted array
        return merge(l_arr_sorted, r_arr_sorted)

    # Base case --> Lists with single elements trivially sorted
    return arr


def merge(l_arr, r_arr):
    # Creating new array to store elements from each half in sorted manner
    arr = [None] * (len(l_arr) + len(r_arr))

    # 2 fingers pointers for each half and one for the main sorted combination
    l_pointer = r_pointer = main_pointer = 0

    while l_pointer < len(l_arr) and r_pointer < len(r_arr):

        # Element from left array added
        if l_arr[l_pointer] < r_arr[r_pointer]:
            arr[main_pointer] = l_arr[l_pointer]
            l_pointer += 1

        # Element from right array added
        else:
            arr[main_pointer] = r_arr[r_pointer]
            r_pointer += 1

        # In any case, one element added to main array
        main_pointer += 1

    # Checking and appending leftover elements in each half
    while l_pointer < len(l_arr):
        arr[main_pointer] = l_arr[l_pointer]
        l_pointer += 1
        main_pointer += 1

    while r_pointer < len(r_arr):
        arr[main_pointer] = r_arr[r_pointer]
        r_pointer += 1
        main_pointer += 1

    return arr


def main():
    arr = [2, 7, 3, 4, 9]
    random_list = random.sample(range(10), 5)

    print("Example list")
    print("1. {}".format(arr))
    print("2. {}".format(merge_sort(arr)))

    print("Random list")
    print("1. {}".format(random_list))
    print("2. {}".format(merge_sort(random_list)))


if __name__ == '__main__':
    main()
