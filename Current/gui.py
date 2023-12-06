# import tkinter as tk
# import numpy as np
# from scipy.optimize import linear_sum_assignment

# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.row_label = tk.Label(self, text="Number of rows:")
#         self.row_label.pack()
#         self.row_entry = tk.Entry(self)
#         self.row_entry.pack()

#         self.col_label = tk.Label(self, text="Number of columns:")
#         self.col_label.pack()
#         self.col_entry = tk.Entry(self)
#         self.col_entry.pack()

#         self.generate_button = tk.Button(self)
#         self.generate_button["text"] = "Generate Matrix"
#         self.generate_button["command"] = self.generate_matrix
#         self.generate_button.pack()

#         self.calculate_button = tk.Button(self)
#         self.calculate_button["text"] = "Calculate"
#         self.calculate_button["command"] = self.calculate
#         self.calculate_button.pack()

#         self.result_text = tk.Text(self)
#         self.result_text.pack()

#     def generate_matrix(self):
#         self.rows = int(self.row_entry.get())
#         self.cols = int(self.col_entry.get())

#         self.matrix_entries = []
#         for i in range(self.rows):
#             row_entries = []
#             for j in range(self.cols):
#                 entry = tk.Entry(self)
#                 entry.pack()
#                 row_entries.append(entry)
#             self.matrix_entries.append(row_entries)

#     def calculate(self):
#         matrix = []
#         for row_entries in self.matrix_entries:
#             row = [int(entry.get()) for entry in row_entries]
#             matrix.append(row)
#         matrix = np.array(matrix)

#         # Perform calculations
#         graph = self.create_bipartite_graph(matrix)
#         row_indices, col_indices = linear_sum_assignment(matrix, maximize=True)
#         max_matching = [(row, col) for row, col in zip(row_indices, col_indices)]
#         updated_matrix = self.switch_matching(matrix.copy(), max_matching)
#         twos_coordinates = self.find_coordinates_of_twos(updated_matrix)
#         coverings = self.find_minimum_coverings(updated_matrix)
#         formatted_coverings = self.format_minimum_coverings(coverings)

#         # Display results
#         self.result_text.insert(tk.END, f"Updated Matrix with a Maximum Matching:\n{updated_matrix}\n")
#         self.result_text.insert(tk.END, f"Max Matching coordinates: Coordinates of '2's in Updated Matrix:\n{twos_coordinates}\n")
#         self.result_text.insert(tk.END, f"Total number of Minimum Coverings: {len(formatted_coverings)}\n")
#         self.result_text.insert(tk.END, f"A Minimum Covering:\n{formatted_coverings}\n")

#     def create_bipartite_graph(self, matrix):
#         row_count, col_count = matrix.shape
#         graph = {}
#         for i in range(row_count):
#             graph[i] = []
#             for j in range(col_count):
#                 if matrix[i][j] != 0:
#                     graph[i].append(j)
#         return graph

#     def switch_matching(self, matrix, max_matching):
#         for match in max_matching:
#             row, col = match
#             if matrix[row][col] == 1:
#                 matrix[row][col] = 2
#         return matrix
import tkinter as tk
import numpy as np
from scipy.optimize import linear_sum_assignment

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.row_label = tk.Label(self, text="Number of rows:")
        self.row_label.pack()
        self.row_entry = tk.Entry(self)
        self.row_entry.pack()

        self.col_label = tk.Label(self, text="Number of columns:")
        self.col_label.pack()
        self.col_entry = tk.Entry(self)
        self.col_entry.pack()

        self.generate_button = tk.Button(self)
        self.generate_button["text"] = "Generate Matrix"
        self.generate_button["command"] = self.generate_matrix
        self.generate_button.pack()

        self.calculate_button = tk.Button(self)
        self.calculate_button["text"] = "Calculate"
        self.calculate_button["command"] = self.calculate
        self.calculate_button.pack()

        self.result_text = tk.Text(self)
        self.result_text.pack()

    def generate_matrix(self):
        self.rows = int(self.row_entry.get())
        self.cols = int(self.col_entry.get())

        self.matrix_entries = []
        for i in range(self.rows):
            row_entries = []
            for j in range(self.cols):
                entry = tk.Entry(self)
                entry.pack()
                row_entries.append(entry)
            self.matrix_entries.append(row_entries)

    def calculate(self):
        self.result_text.delete('1.0', tk.END) # Clear existing content

        matrix = []
        for row_entries in self.matrix_entries:
            row = [int(entry.get()) for entry in row_entries]
            matrix.append(row)
        matrix = np.array(matrix)

        # Perform calculations
        graph = self.create_bipartite_graph(matrix)
        row_indices, col_indices = linear_sum_assignment(matrix, maximize=True)
        max_matching = [(row, col) for row, col in zip(row_indices, col_indices)]
        updated_matrix = self.switch_matching(matrix.copy(), max_matching)
        twos_coordinates = self.find_coordinates_of_twos(updated_matrix)
        coverings = self.find_minimum_coverings(updated_matrix)
        formatted_coverings = self.format_minimum_coverings(coverings)

        # Display results
        self.result_text.insert(tk.END, f"Updated Matrix with a Maximum Matching:\n{updated_matrix}\n")
        self.result_text.insert(tk.END, f"Max Matching coordinates: Coordinates of '2's in Updated Matrix:\n{twos_coordinates}\n")
        self.result_text.insert(tk.END, f"Total number of Minimum Coverings: {len(formatted_coverings)}\n")
        self.result_text.insert(tk.END, f"A Minimum Covering:\n")
        for covering in formatted_coverings:
            self.result_text.insert(tk.END, f"{covering}\n")

    def create_bipartite_graph(self, matrix):
        row_count, col_count = matrix.shape
        graph = {}
        for i in range(row_count):
            graph[i] = []
            for j in range(col_count):
                if matrix[i][j] != 0:
                    graph[i].append(j)
        return graph

    def switch_matching(self, matrix, max_matching):
        for match in max_matching:
            row, col = match
            if matrix[row][col] == 1:
                matrix[row][col] = 2
        return matrix

    def find_coordinates_of_twos(self, matrix):
        twos_coordinates = []
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if matrix[i][j] == 2:
                    twos_coordinates.append((i, chr(65 + j)))
        return twos_coordinates

    def find_minimum_coverings(self, matrix):
        coverings = []
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if matrix[i][j] == 2:
                    coverings.append(f"Column {chr(65 + j)}")
                    break
        return coverings

    def format_minimum_coverings(self, min_coverings):
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

root = tk.Tk()
app = Application(master=root)
app.mainloop()