import numpy as np

class IndependentSetAlgorithm:
    def __init__(self, rows, cols, matrix):
        self.rows = rows
        self.cols = cols
        self.matrix = matrix
        self.col_names = [chr(i) for i in range(ord('A'), ord('A') + cols)]
        self.row_names = [i for i in range(3, 3 + rows)]
    
    def run_algorithm(self):
        # Step 1
        labeled_cols = []
        for j in range(self.cols):
            if 2 not in [self.matrix[i][j] for i in range(self.rows)]:
                labeled_cols.append(j)
        
        # Step 1.1
        new_matrix = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.cols):
                if j in labeled_cols and self.matrix[i][j] == 1:
                    #replace 1 with #
                    new_row.append("#")
                else:
                    new_row.append(self.matrix[i][j])
            new_matrix.append(new_row)
        
        # Step 2
        labeled_rows = []
        while True:
            # Step 2.1
            for j in labeled_cols:
                if j not in labeled_cols:
                    for i in range(self.rows):
                        if self.matrix[i][j] == 2 and i not in labeled_rows:
                            labeled_rows.append(i)
                            self.matrix[i][j] = 3

                    labeled_cols.append(j)

            # Step 2.2
            for i in labeled_rows:
                if i not in labeled_rows:
                    for j in range(self.cols):
                        if self.matrix[i][j] == 2 and j not in labeled_cols:
                            labeled_cols.append(j)
                            self.matrix[i][j] = 4

                    labeled_rows.append(i)

            if all(2 not in self.matrix[i] for i in labeled_rows) or all(j in labeled_cols for j in range(self.cols)):
                break

        # Step 3
        independent_set = []
        for i in range(self.rows):
            if 2 not in self.matrix[i]:
                independent_set.append(i)

        if independent_set:
            # Step 3.1
            path = []
            for i in independent_set:
                for j in range(self.cols):
                    if self.matrix[i][j] == 3:
                        path.append((i, j))
                        break

                if not path:
                    break

                i, j = path[-1]
                if self.matrix[i][j] == 1:
                    break

                for k in range(self.rows):
                    if self.matrix[k][j] == 2 and (k, j) not in path:
                        path.append((k, j))
                        break

                for k in range(self.cols):
                    if self.matrix[i][k] == 1 and (i, k) not in path:
                        path.append((i, k))
                        break

            # Step 3.2
            for i, j in path:
                if self.matrix[i][j] == 1:
                    self.matrix[i][j] = 2
                else:
                    self.matrix[i][j] = 1

            # Step 3.3
            independent_set = []
            for i in range(self.rows):
                if 2 not in self.matrix[i]:
                    independent_set.append(i)

            if independent_set:
                return independent_set
            else:
                return None
        else:
            return None
    
    def print_matrix_columns(self):
        print("The matrix contains " + str(self.cols) + " columns and " + str(self.rows) + " rows.")
        print("Column names and contents:")
        for j in range(self.cols):
            print(f"{self.col_names[j]} [{', '.join(map(str, [self.matrix[i][j] for i in range(self.rows)]))}]")

# Example usage
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
for i in range(rows):
    row = list(map(int, input(f"Enter the numbers (0,1,or 2) for Row {i+1}: ").split()))
    matrix.append(row)

algorithm = IndependentSetAlgorithm(rows, cols, matrix)
algorithm.print_matrix()
independent_set = algorithm.run_algorithm()
if independent_set:
    print("The present independent set is:")
    for i in independent_set:
        print(f"{algorithm.row_names[i]}")
    print("The present independent set is a maximum independent set.")
else:
    print("No independent set found")



algorithm.print_matrix_columns()
'''
   A B C D 
3 [2, 0, 1, 1]
4 [0, 2, 0, 0]
5 [1, 1, 0, 0]
6 [0, 1, 0, 0]


Would appear as:

A [2, 0, 1, 0]
B [0, 2, 1, 1]
C [1, 0, 0, 0]
D [1, 0, 0, 0]
'''