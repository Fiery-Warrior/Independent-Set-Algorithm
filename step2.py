def step2(matrix, labeled_cols, rows, cols, row_names, col_names):
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
