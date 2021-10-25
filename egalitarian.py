import cvxpy

def egalitarian_division(matrix: list):
        m = len(matrix[0])
        n = len(matrix)
        all_var, constraints = [[cvxpy.Variable() for _ in range(m)] for _ in range(n)], []
        z = cvxpy.Variable()
       
        for i in range(n):
            temp = 0
            for j in range(m):
                temp += matrix[i][j] *all_var[i][j] 
                constraints.append(all_var[i][j] >= 0)
            constraints.append(temp >= z)

        for j in range(m):
            temp = 0
            for i in range(n):
                temp +=  all_var[i][j]
            constraints.append(temp == 1)

        prob = cvxpy.Problem(cvxpy.Maximize(z), constraints)
        prob.solve()

        for i in range(n):
            print("Agent #{} ".format(i + 1), end='')
            for j in range(m):
                print(" gets {:.2f} of resource #{}".format(all_var[i][j].value, j + 1), end='')
                print(',' if (j + 1) != m else '.\n', end='')

def main():
    mat = [
        [81, 19, 1],
        [70, 1, 29],
    ]

    egalitarian_division(mat)

if __name__ == '__main__':
    main()