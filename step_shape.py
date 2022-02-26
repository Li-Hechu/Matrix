from log import filelog
from fractions import Fraction


class Matrix_Step_Shape:
    def init(n, m, arr:list):
        Matrix_Step_Shape.arr = arr
        Matrix_Step_Shape.n = n
        Matrix_Step_Shape.m = m

    def down(n, m, arr:list):
        '''下半部分化为阶梯型'''
        a = 0  # 公因数
        Matrix_Step_Shape.order()
        if n <= m:
            loop = n - 1
        else:
            loop = m
        for i in range(loop):
            start = Matrix_Step_Shape.detect1(i)
            if start == m:
                break
            else:
                for j in range(i + 1, n, 1):
                    a = Fraction(arr[j][start], arr[i][start])
                    for k in range(start, m, 1):
                        arr[j][k] = arr[j][k] - arr[i][k] * a
                Matrix_Step_Shape.order()
            start = 0
        Matrix_Step_Shape.order()
        filelog("阶梯型化简完成。")
        return arr

    def up(n, m, arr:list):
        '''上半部分化为阶梯型'''
        b = 0  # 公因数
        end_row = Matrix_Step_Shape.detect2()
        for i in range(end_row, 0, -1):
            begin = Matrix_Step_Shape.detect1(i)
            for j in range(i - 1, -1, -1):
                b = Fraction(arr[j][begin], arr[i][begin])
                for k in range(begin, m, 1):
                    arr[j][k] = arr[j][k] - arr[i][k] * b
            begin = 0
        filelog("行简化阶梯型化简完成。")
        return arr

    def order():
        '''根据0出现的位置进行阶梯型排序'''
        for i in range(0, Matrix_Step_Shape.n - 1, 1):
            for j in range(i + 1, Matrix_Step_Shape.n, 1):
                if Matrix_Step_Shape.detect1(i) > Matrix_Step_Shape.detect1(j):
                    Matrix_Step_Shape.arr[i], Matrix_Step_Shape.arr[j] = \
                        Matrix_Step_Shape.arr[j], Matrix_Step_Shape.arr[i]

    def detect1(row):
        '''检测每行非0元素的起始位置'''
        start = 0
        for i in range(Matrix_Step_Shape.m):
            if Matrix_Step_Shape.arr[row][i] == 0:
                start += 1
            else:
                break
        return start

    def detect2():
        '''检测最后一个非0行的索引'''
        end_row = 0
        for i in range(Matrix_Step_Shape.n):
            for j in range(Matrix_Step_Shape.m):
                if Matrix_Step_Shape.arr[i][j] != 0:
                    end_row += 1
                    break
        return end_row - 1
