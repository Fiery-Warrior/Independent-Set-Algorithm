class IndependentSetAlgorithm:
    """
    This class implements the independent set algorithm. 
    It takes a matrix as input and returns the final matrix after running the algorithm.
    """
    def __init__(self, rows, cols, matrix):
        """
        Initializes the IndependentSetAlgorithm class with the given rows, columns, and matrix.
        :param rows: number of rows in the matrix
        :type rows: int
        :param cols: number of columns in the matrix
        :type cols: int
        :param matrix: matrix to run the algorithm on
        :type matrix: list[list[int]]
        """
        self.rows = rows
        self.cols = cols
        self.matrix = matrix
        self.col_names = [chr(i) for i in range(ord('A'), ord('A') + cols)]
        self.row_names = [i for i in range(3, 3 + rows)]
    
    def run_algorithm(self):
        """
        Runs the independent set algorithm on the given matrix.
        """
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
                    #replace 1 with '#' (hash)
                    new_row.append("#")
                else:
                    new_row.append(str(self.matrix[i][j])) # convert integer to string
            new_matrix.append(new_row)
        
        # Step 1.2
        print("\nLabeled matrix with '#'s where there are no 2s in a column:")
        print_matrix(new_matrix, self.row_names, self.col_names)
        print("Put # (hashes) at bottom of columns:")
        for j in labeled_cols:
            print(f"{self.col_names[j]}")
            
        
        # Step 2 --NOT
        labeled_rows = []
        while True:
            # Step 2.1 --NOT
            for j in labeled_cols:
                if j not in labeled_cols:
                    for i in range(self.rows):
                        if self.matrix[i][j] == 2 and i not in labeled_rows:
                            labeled_rows.append(i)
                            self.matrix[i][j] = 3
                            print(f"{self.row_names[i]}{self.col_names[j]}")

                    labeled_cols.append(j)

            # Step 2.2 --NOT
            for i in labeled_rows:
                if i not in labeled_rows:
                    for j in range(self.cols):
                        if self.matrix[i][j] == 2 and j not in labeled_cols:
                            labeled_cols.append(j)
                            self.matrix[i][j] = 4
                            print(f"{self.row_names[i]}{self.col_names[j]}")

                    labeled_rows.append(i)

            if all(2 not in self.matrix[i] for i in labeled_rows) or all(j in labeled_cols for j in range(self.cols)):
                break
        
        # Real Step 2
        '''
        Should look at all columns with '#'s (1s with no 2 in the column) then label that row with the name of the column being scanned. 
        
        Then Mark with a Name 'A' or 'B' or 'C' etc... (by putting the column with the # to indicate that it has been scanned) put the column name on the the row side on the right side of the matrix
        '''
        # Step 2.1
        print("\nStep 2.1: Label the rows with # and put column names outside the matrix (aligned on the side of the row) then as a user mark the # with a checkmark to indicate that it has been scanned:")
        for i in range(self.rows):
            if "#" in new_matrix[i]:
                col_index = new_matrix[i].index("#")
                col_name = self.col_names[col_index]
                row_name = self.row_names[i]
                new_matrix[i][col_index] = "#" # keep the checkmark
                print(f"Label row: {row_name} with the column name: {col_name}")
                new_matrix[i].append(col_name) # add the column name to the end of the row
                print(f"{row_name} {col_name}")
                print_matrix(new_matrix, self.row_names, self.col_names)


        
        # print_matrix(self.matrix, self.row_names, self.col_names)
        print("**********Ignore*************************************************************")
        print("Some information about the matrix: new_matrix, self.row_names, self.col_names")
        print("******************************************************************************")


        print("\nStep 2.2: Go to the row with a #. in it then go to the column that has a 2 and record which name of the row the 2 is in. Then put the name of the row at the bottom of that column:")
        for i in range(self.rows):
            if "#" in new_matrix[i]:
                col_index = new_matrix[i].index("#")
                for j in range(self.cols):
                    if self.matrix[i][j] == 2:
                        row_name = self.row_names[i]
                        col_name = self.col_names[j]
                        print(f"row: {row_name} and column: {col_name}")
                        # new_matrix[self.rows-1][j] = row_name # this replaces the last 0 of the column 2 with row name
                        print(f"write the name of row {row_name} at the bottom of column {col_name}")
                        break

                    #inside ALL columns with a 2 if there are 1s in that column then make sure that you mark the row with that 1 with the name of the column (this would be typed outside the matrix on the right side of the matrix)
        
        print_matrix(new_matrix, self.row_names, self.col_names)
        
    def print_matrix(self):
        """
        Prints the matrix with row and column names.
        """
        print("\nThe matrix contains " + str(self.cols) + " columns and " + str(self.rows) + " rows.\n")
        print_matrix(self.matrix, self.row_names, self.col_names)

def print_matrix(matrix, row_names, col_names):
    print("   " + " ".join([f"{col_names[j]} " for j in range(len(col_names))]))
    for i in range(len(matrix)):
        print(f"{row_names[i]} [{', '.join(map(str, matrix[i]))}]")





# Program starts here
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
for i in range(rows):
    row = list(map(int, input(f"Enter the numbers (0,1,or 2) for Row {i+1}: ").split()))
    matrix.append(row)


algorithm = IndependentSetAlgorithm(rows, cols, matrix)
algorithm.print_matrix()
algorithm.run_algorithm()
