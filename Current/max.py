import numpy as np
from scipy.optimize import linear_sum_assignment

def create_bipartite_graph(matrix):
    row_count, col_count = matrix.shape
    graph = {}
    for i in range(row_count):
        graph[i] = []
        for j in range(col_count):
            if matrix[i][j] != 0:
                graph[i].append(j)
    return graph

def print_matrix(matrix):
    row_count, col_count = matrix.shape
    print("\nThe matrix contains {} columns and {} rows.\n".format(col_count, row_count))
    print("   ", "  ".join([chr(65 + i) for i in range(col_count)]))
    for i, row in enumerate(matrix, start=1):
        print(f"{i} {row}")

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print("Enter the numbers ('1', 'stared 1', or '2') for each row:")

    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter the numbers for Row {i+1}: ").split()))
        matrix.append(row)
    matrix = np.array(matrix)

    print_matrix(matrix)

    # Step 1: Create the bipartite graph
    graph = create_bipartite_graph(matrix)

    # Step 2: Perform maximum matching using Hungarian algorithm
    row_indices, col_indices = linear_sum_assignment(matrix, maximize=True)
    max_matching = [(row, col) for row, col in zip(row_indices, col_indices)]

    print("\nMaximum Matching:")
    for match in max_matching:
        print(f"Row {match[0]+1} matches with Column {chr(65 + match[1])}")

    # Step 3: Find minimum covering
    min_covering = set(range(rows))
    for match in max_matching:
        min_covering.discard(match[0])

    print("\nMinimum Covering:")
    for row in min_covering:
        print(f"Row {row+1}")

if __name__ == "__main__":
    main()
