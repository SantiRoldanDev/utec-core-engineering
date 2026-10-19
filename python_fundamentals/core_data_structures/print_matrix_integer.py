#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for j in range(len(row)):
            if j < len(row) - 1:
                print("{:d}".format(row[j]), end=" ")
            else:
                print("{:d}".format(row[j]), end="")
        print()


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_matrix_integer(matrix)
