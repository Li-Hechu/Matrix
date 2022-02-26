from step_shape import Matrix_Step_Shape
from log import filelog
from fractions import Fraction


class Matrix_Inverse:
    def init(n, m, arr:list):
        arr1 = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            arr1[i][i] = 1  # 初始化单位矩阵
            arr[i].extend(arr1[i])  # 完成合并
        return arr

    def result(n, m, arr:list):
        arr1 = Matrix_Inverse.init(n, m, arr)
        Matrix_Step_Shape.init(n, m, arr1)
        temp_arr = Matrix_Step_Shape.down(n, 2*m, arr1)
        end_row = Matrix_Step_Shape.detect2()
        if end_row != n - 1:
            filelog("您所输入的矩阵不可逆。")
            print("该矩阵不满秩，不可逆。")
            return temp_arr
        arr2 = Matrix_Step_Shape.up(n, 2*m, temp_arr)
        # 把前面化为单位矩阵
        for i in range(n - 1, -1, -1):
            for j in range(m, 2 * m, 1):
                arr2[i][j] = Fraction(arr2[i][j], arr2[i][i])
        # 去除前面的单位矩阵
        for i in range(n):
            for j in range(m):
                del arr2[i][j]
        filelog("矩阵运算完成")
        return arr2
