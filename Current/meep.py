class IndependentSetAlgorithm:

    def __init__(self, rows, cols, matrix):
        self.rows = rows
        self.cols = cols
        self.matrix = matrix
        self.col_names = [chr(i) for i in range(ord('A'), ord('A') + cols)]
        self.row_names = [i for i in range(3, 3 + rows)]

    def run_algorithm(self):
        labeled_rows = []
        labeled_cols = []

        while True:
            new_labeled_cols = []
            new_labeled_rows = []

            # Step 2.1
            for j in range(self.cols):
                if j not in labeled_cols:
                    for i in range(self.rows):
                        if self.matrix[i][j] == 'stared 1' and i not in labeled_rows:
                            new_labeled_cols.append(j)
                            new_labeled_rows.append(i)
                            print(f"Label row {self.row_names[i]} with {self.col_names[j]} (in column {self.col_names[j]})")
                            print(f"Mark column {self.col_names[j]} indicating scanned.\n")

            labeled_cols.extend(new_labeled_cols)
            labeled_rows.extend(new_labeled_rows)

            new_labeled_cols = []
            # Step 2.2
            for i in range(self.rows):
                if i not in labeled_rows:
                    for j in range(self.cols):
                        if self.matrix[i][j] == '1' and j in labeled_cols:
                            new_labeled_cols.append(j)
                            labeled_cols.append(j)
                            labeled_rows.append(i)
                            print(f"Label column {self.col_names[j]} with {self.row_names[i]} (in row {self.row_names[i]})")
                            print(f"Mark row {self.row_names[i]} indicating scanned.\n")

            if all('stared 1' not in self.matrix[i] for i in labeled_rows) or all(j in labeled_cols for j in range(self.cols)):
                break

        print("\nThe matrix after Step 2:")
        self.print_matrix(self.matrix)

        # Step 3
        while True:
            labeled_row_without_stared_1 = None
            for i in labeled_rows:
                if '1' in self.matrix[i] and 'stared 1' not in self.matrix[i]:
                    labeled_row_without_stared_1 = i
                    break

            if labeled_row_without_stared_1 is None:
                print("Step 3.3 (No Improvement)")
                break

            current_row = labeled_row_without_stared_1
            current_col = self.matrix[current_row].index('1')
            self.matrix[current_row][current_col] = '1!'

            while True:
                next_col = self.matrix[current_row].index('stared 1')
                self.matrix[current_row][next_col] = 'stared 1!'
                current_row = [self.matrix[i][next_col] for i in range(self.rows)].index('stared 1')
                self.matrix[current_row][next_col] = 'stared 1!'

                if '1' in self.matrix[current_row] and 'stared 1' not in self.matrix[current_row]:
                    current_col = self.matrix[current_row].index('1')
                    self.matrix[current_row][current_col] = '1!'
                else:
                    break

        print("\nThe matrix after Step 3:")
        self.print_matrix(self.matrix)

    def print_matrix(self, matrix):
        print(f"\nThe matrix contains {self.cols} columns and {self.rows} rows.\n")
        print("   " + " ".join([f"{self.col_names[j]} " for j in range(self.cols)]))
        for i in range(self.rows):
            print(f"{self.row_names[i]} [{', '.join(map(str, matrix[i]))}]")

# Take user input
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
for i in range(rows):
    row = input(f"Enter the numbers ('1', 'stared 1', or '2') for Row {i+1}: ").split()
    matrix.append(row)

algorithm = IndependentSetAlgorithm(rows, cols, matrix)
algorithm.run_algorithm()
