from Heaps import heap
import random


def heap_sort(unsorted_arr):
    # Converting unsorted array to a Max Heap
    heap_arr = heap.Heap(unsorted_arr, len(unsorted_arr) - 1)
    heap_arr.build_max_heap()

    # Needed to store elements in correct order
    sorted_arr = [None] * heap_arr.n
    sorted_arr_index = heap_arr.n - 1

    while not heap_arr.is_empty():

        # Storing highest element in new array, ascending order maintained
        max_element = heap_arr.heap[1]
        sorted_arr[sorted_arr_index] = max_element
        sorted_arr_index -= 1

        # Removing root from heap by exchanging with last leaf
        heap_arr.heap[1], heap_arr.heap[heap_arr.n] = heap_arr.heap[heap_arr.n], heap_arr.heap[1]
        heap_arr.n -= 1

        # Above exchange may violate Max Heap property at root, correcting
        heap_arr.max_heapify(1)

    return sorted_arr


def main():
    # Index 0 is ignored
    unsorted_arr = random.sample(range(20), 11)
    unsorted_arr[0] = -1

    print("Unsorted array:\n", unsorted_arr[1:])
    print("Sorted array:\n", heap_sort(unsorted_arr))


if __name__ == '__main__':
    main()
