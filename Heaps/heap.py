import math

# Lambda exps for simple tree index calculations
level = lambda index: int(math.log2(index))
is_root = lambda index: index == 1
parent = lambda index: index // 2
left = lambda index: 2 * index
right = lambda index: 2 * index + 1


class Heap:

    # Element at index 0 ignored to keep index calculation simple
    def __init__(self, heap, n):
        self.heap = heap
        self.n = n

    def is_empty(self):
        return self.n == 0

    def build_max_heap(self):
        """
        Produces a max heap from an unordered array
        """
        for index in range(self.n // 2, 0, -1):
            self.max_heapify(index)

    def max_heapify(self, index):
        """
        Corrects a single violation of the max heap property
        in a subtree's root
        """

        # Indexes of left and right children
        l = left(index)
        r = right(index)

        # Index of greatest among parent and two children, needed to decide if heapify required
        largest_index = index

        # Left child greatest
        if l <= self.n and self.heap[l] > self.heap[index]:
            largest_index = l

        # Right child greatest
        if r <= self.n and self.heap[r] > self.heap[largest_index]:
            largest_index = r

        # Max Heap property violated, swap done and corresponding subtree heapified
        if largest_index != index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.max_heapify(largest_index)


def main():
    heap_array = [-1, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    myHeap = Heap(heap_array, len(heap_array)-1)

    myHeap.build_max_heap()
    print(myHeap.heap)


if __name__ == '__main__':
    main()
