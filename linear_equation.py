from log import filelog
from step_shape import Matrix_Step_Shape


class Matrix_Linear_Equation:
    def result(n,m,arr):
        Matrix_Step_Shape.init(n,m,arr)
        temp = Matrix_Step_Shape.down(n,m,arr)
        end_row = Matrix_Step_Shape.detect2()
        if Matrix_Step_Shape.detect1(end_row) == m - 1:
            print("该方程组无解，其阶梯型为：")
            filelog("输入的方程组无解。")
            filelog("矩阵运算完成。")
            return temp
        final = Matrix_Step_Shape.up(n,m,temp)
        filelog("矩阵运算完成。")
        return final
