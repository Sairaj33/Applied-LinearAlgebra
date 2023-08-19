def print_matrix(matrix):
    for row in matrix:
        print(row)

def gaussian_elimination(A, b):
    n = len(A)
    
    # Augmented matrix i.e, mat and vec
    aug_mat = [row_a + [row_b] for row_a, row_b in zip(A, b)]
     
    for i in range(n):
        #maximum absolute value in the current column
        max_row = i
        for j in range(i + 1, n):
            if abs(aug_mat[j][i]) > abs(aug_mat[max_row][i]):
                max_row = j
        
        # Swap rows if neccessary
        aug_mat[i], aug_mat[max_row] = aug_mat[max_row], aug_mat[i]
        
        # Check if it is consistent or inconsistent
        if aug_mat[i][i] == 0:
            return None  # if none means inconsistent       
        # Make the diagonal element 1 for further operations 
        pivot = aug_mat[i][i]
        for j in range(i, n + 1):
            aug_mat[i][j] /= pivot      
        # Making other rows zero
        for j in range(n):
            if j != i:
                factor = aug_mat[j][i]
                for k in range(i, n + 1):
                    aug_mat[j][k] -= factor * aug_mat[i][k]   
    #Final solution
    solutions = [row[-1] for row in aug_mat]   
    return solutions

# Take order and the values of the matrix as input
matrix_order = int(input("Enter the matrix order (number of rows or columns): "))
print("Enter matrix A elements:")
A = []
for _ in range(matrix_order):
    row = [int(x) for x in input().split()]
    A.append(row)

# vector b  as input
print("Enter vector b elements:")
b = [int(x) for x in input().split()]
solution = gaussian_elimination(A, b)# final ans
if solution is None:
    print("The system of equations is inconsistent.")
else:
    print("Solution:", solution)


