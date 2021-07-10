fibo_matrix = [[1, 1], [1, 0]]
P = 10 ** 6


def mul_matrix(matrix1, matrix2):
    new_matrix = []
    for i in range(2):
        row = [
            sum(matrix1[i][k] * matrix2[k][j] for k in range(2)) % P for j in range(2)
        ]
        new_matrix.append(row)

    return new_matrix


def div_conq(n):
    if n == 1:
        return fibo_matrix
    elif n % 2:
        return mul_matrix(div_conq(n - 1), fibo_matrix)
    else:
        cur_matrix = div_conq(n // 2)
        return mul_matrix(cur_matrix, cur_matrix)


N = int(input())
if N == 1:
    print(1)
else:
    print(div_conq(N - 1)[0][0])
