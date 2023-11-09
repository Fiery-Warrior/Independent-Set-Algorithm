# import numpy as np

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
                    new_row.append(str(self.matrix[i][j])) # convert integer to string
            new_matrix.append(new_row)
        
        # Step 1.2
        print("Labeled matrix with #s where there are no 2s in a column:")
        print_matrix(new_matrix, self.row_names, self.col_names)
        print("Put # (hashes) at bottom of columns:")
        for j in labeled_cols:
            print(f"{self.col_names[j]}")
        
    def print_matrix(self):
        print("The matrix contains " + str(self.cols) + " columns and " + str(self.rows) + " rows.")
        print_matrix(self.matrix, self.row_names, self.col_names)

def print_matrix(matrix, row_names, col_names):
    print("   " + " ".join([f"{col_names[j]} " for j in range(len(col_names))]))
    for i in range(len(matrix)):
        print(f"{row_names[i]} [{', '.join(map(str, matrix[i]))}]")

# Example usage
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
for i in range(rows):
    row = list(map(int, input(f"Enter the numbers (0,1,or 2) for Row {i+1}: ").split()))
    matrix.append(row)

algorithm = IndependentSetAlgorithm(rows, cols, matrix)
algorithm.print_matrix()
algorithm.run_algorithm()
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