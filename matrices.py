# The element aij of the matrix A is A[i][j]
# For the mathematical connvention we use capital letter
# to designate a matrix

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0])
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [i[j] for i in A]

def make_matrix(num_rows, num_cols, generator_function):
    tt = []
    for i in range(num_rows):
        t = []
        for j in range(num_cols):
            t.append(generator_function(i,j))
        tt.append(t)
    return tt

# example of making a matrix from the function above
def is_diagonal(i, j):
    return 1 if i == j else 0


if __name__ == '__main__':
    A = [[1, 2, 3],
         [4, 5, 6]]

    B = [[1, 2],
         [3, 4],
         [5, 6]]

    print(shape(A))
    print(get_row(A, 1))
    print(get_column(A, 2))
    print(make_matrix(5, 5, is_diagonal))