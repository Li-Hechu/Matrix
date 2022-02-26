import sympy
from fractions import Fraction
from determinant import *
from log import filelog

x = sympy.symbols("x")


class Matrix_Character_Value:
    def result(n, m, arr):
        arr1 = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            arr1[i][i] = x
            for j in range(m):
                arr[i][j] = arr1[i][j] - arr[i][j]
        Matrix_Determinant.init(n,m,arr)
        sum = Matrix_Determinant.result(n,arr)
        answer = sympy.solve([sum],[x])
        filelog("特征值求解完成。")
        return answer