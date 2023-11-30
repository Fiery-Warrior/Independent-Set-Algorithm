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
    print("  ", " ".join([chr(65 + i) for i in range(col_count)])) #also in charge spacing for the column names and where the column names are initally printed
    for i, row in enumerate(matrix, start=1):
        print(f"{i} {row}")

def switch_matching(matrix, max_matching):
    # for match in max_matching[:-1]:  # Exclude the last match
    for match in max_matching[:]:  # does not Exclude the last match
        row, col = match
        if matrix[row][col] == 0 or matrix[row][col] == 1:
            matrix[row][col] = 2
    return matrix

def get_user_input():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print("Enter the numbers ('1', 'stared 1', or '2') for each row:")
    
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter the numbers for Row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

def find_minimum_coverings(matrix):
    coverings = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j] == 2:
                coverings.append(f"Row {i+1}")
                coverings.append(f"Column {chr(65 + j)}")
                break
    return coverings

def format_minimum_coverings(min_coverings):
    formatted_coverings = []
    temp = set()
    for covering in min_coverings:
        if covering.startswith("Row"):
            temp.add(covering)
        else:
            temp.add(covering.split()[1])
            formatted_coverings.append(", ".join(sorted(temp)))
            temp = set()
    return formatted_coverings

def main():
    matrix = get_user_input()
    print_matrix(matrix)

    # Step 1: Create the bipartite graph
    graph = create_bipartite_graph(matrix)

    # Step 2: Perform maximum matching using ISA algorithm
    row_indices, col_indices = linear_sum_assignment(matrix, maximize=True)
    max_matching = [(row, col) for row, col in zip(row_indices, col_indices)]

    print("\nMaximum Matching:")
    # for match in max_matching[:-1]:  # Exclude the last match
    for match in max_matching[:]:  # does not Exclude the last match
        print(f"Row {match[0]+1} matches with Column {chr(65 + match[1])}")

    # Switch ones or zeros at maximum matching coordinates with 2s
    updated_matrix = switch_matching(matrix.copy(), max_matching)

    # Display the updated matrix
    print("\nUpdated Matrix with Maximum Matching:")
    print_matrix(updated_matrix)

    # Step 3: Find minimum covering
    coverings = find_minimum_coverings(updated_matrix)
    formatted_coverings = format_minimum_coverings(coverings)
    print(f"\nTotal number of Minimum Coverings: {len(formatted_coverings)}")
    print("\nMinimum Coverings:")
    for covering in formatted_coverings:
        print(f"{covering}")

if __name__ == "__main__":
    main()
