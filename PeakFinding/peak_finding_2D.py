import numpy as np


# returns index of highest element in a given column
def get_column_max_index(arr, col_num):
    return arr[:, col_num].argmax()


# Complexity --> \theta (n log m), n = number of rows, m = number of columns
def peak_finder(arr, min_col, max_col):

    # column to be considered
    col_num = int(min_col + (max_col - min_col) / 2)

    # getting the row index of highest element in selected column
    max_row_index = get_column_max_index(arr, col_num)

    # if left neighbour is greater than highest element of selected column,
    # columns on the left have a peak
    if col_num > 0 and arr[max_row_index, col_num] < arr[max_row_index, col_num - 1]:
        return peak_finder(arr, min_col, col_num - 1)

    # if right neighbour of that number is greater, columns on the right have a peak
    elif col_num < arr.shape[0] - 1 and arr[max_row_index, col_num] < arr[max_row_index, col_num + 1]:
        return peak_finder(arr, col_num + 1, max_col)

    # when number is highest in column AND (left and right neighbours smaller OR no columns left)
    else:
        return max_row_index, col_num


def main():
    # Creating 4x4 NumPy array used in Course booklet
    example_matrix = np.array([10, 8, 10, 10,
                               14, 13, 12, 11,
                               15, 9, 11, 21,
                               16, 17, 19, 20]).reshape(4, 4)

    print(example_matrix)
    print("Peak index: ", peak_finder(example_matrix, 0, 3))
    print()
    # Creating a random 5x5 NumPy array
    example_matrix2 = np.random.randint(30, size=(5, 5))
    print(example_matrix2)
    print("Peak index: ", peak_finder(example_matrix2, 0, 4))


if __name__ == '__main__':
    main()
