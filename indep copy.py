import numpy as np

print("This program works as follows:")
print("Type 0: for no edge")
print("Type 1: for edge")
print("Type 2: in place of 1* for current edge, as part of matching")

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
for i in range(rows):
    row = list(map(int, input(f"Enter the numbers (0,1,or 2) for Row {i+1}: ").split()))
    matrix.append(row)


# Step 0.1
col_names = [chr(i) for i in range(ord('A'), ord('A') + cols)]
row_names = [i for i in range(3, 3 + rows)]

print("Labeled matrix:")
print("   ", end="")
for col in col_names:
    print(col, end=" ")
print()
for i, row in enumerate(matrix):
    print(f"{row_names[i]} [{', '.join(map(str, row))}]")

print("Type 'done' to calculate")
command = input()
if command.lower() == 'done':
    # Step 1
    print("step 1:")
    print("Labeling with # on columns with no 2s (unstared 1s) ::")
    labeled_cols = []
    for j in range(cols):
        if 2 not in [matrix[i][j] for i in range(rows)]:
            labeled_cols.append(j)
            print(f"#{col_names[j]}", end=" ")
    print()
    print("   ", end="")
    for col in col_names:
        print(col, end=" ")
    print()
    for i, row in enumerate(matrix):
        print(f"{row_names[i]} [{', '.join(map(str, row))}]")
    
    # Step 1.1
    new_matrix = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            if j in labeled_cols and matrix[i][j] == 1:
                #replace 1 with #
                new_row.append("#")
            else:
                new_row.append(matrix[i][j])
        new_matrix.append(new_row)
    
    # Print new matrix
    print("New matrix after step 1:")
    print("   ", end="")
    for col in col_names:
        print(col, end=" ")
    print()
    for i, row in enumerate(new_matrix):
        print(f"{row_names[i]} [{', '.join(map(str, row))}]")

    # Step 2
    print("\nStep 2:")
    labeled_rows = []
    while True:
        # Step 2.1
        for j in labeled_cols:
            if j not in labeled_cols:
                for i in range(rows):
                    if matrix[i][j] == 2 and i not in labeled_rows:
                        labeled_rows.append(i)
                        matrix[i][j] = 3
                        print(f"{row_names[i]}{col_names[j]}")

                labeled_cols.append(j)

        # Step 2.2
        for i in labeled_rows:
            if i not in labeled_rows:
                for j in range(cols):
                    if matrix[i][j] == 2 and j not in labeled_cols:
                        labeled_cols.append(j)
                        matrix[i][j] = 4
                        print(f"{row_names[i]}{col_names[j]}")

                labeled_rows.append(i)

        if all(2 not in matrix[i] for i in labeled_rows) or all(j in labeled_cols for j in range(cols)):
            break

    # Step 3
    independent_set = []
    for i in range(rows):
        if 2 not in matrix[i]:
            independent_set.append(i)
            print(f"{row_names[i]}")

    if independent_set:
        # Step 3.1
        path = []
        for i in independent_set:
            for j in range(cols):
                if matrix[i][j] == 3:
                    path.append((i, j))
                    break

            if not path:
                break

            i, j = path[-1]
            if matrix[i][j] == 1:
                break

            for k in range(rows):
                if matrix[k][j] == 2 and (k, j) not in path:
                    path.append((k, j))
                    break

            for k in range(cols):
                if matrix[i][k] == 1 and (i, k) not in path:
                    path.append((i, k))
                    break

        # Step 3.2
        for i, j in path:
            if matrix[i][j] == 1:
                matrix[i][j] = 2
            else:
                matrix[i][j] = 1

        # Step 3.3
        independent_set = []
        for i in range(rows):
            if 2 not in matrix[i]:
                independent_set.append(i)

        print("Maximum independent set:")
        for i in independent_set:
            print(f"{row_names[i]}")
    else:
        print("No independent set found")        
    if independent_set:
        print("The present independent set is:")
        for i in independent_set:
            print(f"{row_names[i]}")
        print("The present independent set is a maximum independent set.")
    else:
        print("No independent set found")

    # New look of the matrix after assigning names to columns and rows
    print("New look of the matrix:")
    print("   ", end="")
    for col in col_names:
        print(col, end=" ")
    print()
    for i, row in enumerate(matrix):
        print(f"{row_names[i]} [{', '.join(map(str, row))}]")
