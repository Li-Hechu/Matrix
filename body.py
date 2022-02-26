from log import filelog
from input import Matrix_Input
from sum import Matrix_Sum
from multiple import Matrix_Multiple
from transpose import Matrix_Transpose
from step_shape import Matrix_Step_Shape
from inverse import Matrix_Inverse
from linear_equation import Matrix_Linear_Equation
from determinant import Matrix_Determinant
from character_value import Matrix_Character_Value


class Function_Body:
    '''这个模块包含该系统的所有功能'''

    def __init__(self):
        filelog("您已开始程序。")
        print("-"*15+"欢迎使用纯数组矩阵运算系统"+"-"*15)
        print("-"*56)
        print(" "*26+"说明"+" "*26)
        print("1.该程序由LHC设计，未经允许，不得转载、复制和传播。")
        print("2.该系统仅使用数组进行计算，没有使用矩阵计算模块。")
        print("  但是为了实现某些特定功能，会使用其他科学计算模块。")
        print("3.该系统现在支持矩阵加法和乘法，矩阵求逆，矩阵的转置，")
        print("  矩阵的行列式计算，矩阵的特征值计算以及矩阵阶梯型和")
        print("  行简化阶梯型（求解线性方程组）的计算。更多功能正在")
        print("  开发中，敬请期待。")
        print("4.请根据屏幕提示完成相应操作。")
        print("5.在提示输入功能序号时输入0以结束程序。")
        print("6.在本目录下有一个名为filelog.log的日志文件，用来记录")
        print("  您的每一步操作，如果该文件太大，请手动删除。")
        print("-"*56)

    def begin(self):
        input("按下回车键以开始。")
        print("-"*56)
        print("各个功能的序号如下：")
        print("矩阵的加法：1"+" "*5, end="")
        print("矩阵的乘法：2"+" "*5, end="")
        print("矩阵求逆：3")
        print("矩阵转置：4"+" "*5, end="")
        print("矩阵的阶梯型：5"+" "*3, end="")
        print("矩阵的行简化阶梯型：6")
        print("矩阵的行列式：7"+" "*5, end="")
        print("矩阵的特征值：8"+" "*5)

    def target(self):
        '''输入功能序号'''
        num = int(input("根据功能序号，请输入您需要求的内容："))
        if num == 0:
            consequence = "退出程序。。。程序已退出。"
        elif num == 1:
            consequence = "矩阵相加"
        elif num == 2:
            consequence = "矩阵相乘"
        elif num == 3:
            consequence = "矩阵求逆"
        elif num == 4:
            consequence = "矩阵转置"
        elif num == 5:
            consequence = "矩阵的阶梯型"
        elif num == 6:
            consequence = "矩阵的行简化阶梯型"
        elif num == 7:
            consequence = "矩阵的行列式"
        elif num == 8:
            consequence = "矩阵的特征值"
        filelog("您选择了"+consequence)
        return num

    def write(self, num):
        '''输入矩阵'''
        Matrix_Input.flush()
        Matrix_Input.init(num)
        self.n = Matrix_Input.n
        self.m = Matrix_Input.m
        self.p = Matrix_Input.p
        self.q = Matrix_Input.q
        if num == 3 or num == 4 or num == 5 or num == 6 or num == 7 or num == 8:
            Matrix_Input.one()
            self.arr = Matrix_Input.arr1
        elif num == 1:
            Matrix_Input.two()
            self.arr1 = Matrix_Input.arr1
            self.arr2 = Matrix_Input.arr2
        elif num == 2:
            while self.m != self.p:
                print("您输入的矩阵无法相乘，请重新输入。")
                filelog("您输入导入矩阵无法相乘。")
                Matrix_Input.init(num)
                self.n = Matrix_Input.n
                self.m = Matrix_Input.m
                self.p = Matrix_Input.p
                self.q = Matrix_Input.q
            Matrix_Input.two()
            self.arr1 = Matrix_Input.arr1
            self.arr2 = Matrix_Input.arr2

    def sum(self):
        '''矩阵求和'''
        result = Matrix_Sum.result(self.n, self.m, self.arr1, self.arr2)
        return result

    def multiple(self):
        '''矩阵相乘'''
        result = Matrix_Multiple.result(
            self.n, self.q, self.m, self.arr1, self.arr2)
        return result

    def transpose(self):
        '''矩阵转置'''
        result = Matrix_Transpose.result(self.n, self.m, self.arr)
        return result

    def step_shape(self):
        '''矩阵的阶梯型'''
        Matrix_Step_Shape.init(self.n, self.m, self.arr)
        result = Matrix_Step_Shape.down(self.n, self.m, self.arr)
        return result

    def inverse(self):
        '''矩阵求逆'''
        result = Matrix_Inverse.result(self.n, self.m, self.arr)
        return result

    def linear_equation(self):
        '''行简化阶梯型'''
        result = Matrix_Linear_Equation.result(self.n, self.m, self.arr)
        return result

    def determinant(self):
        '''矩阵的行列式'''
        Matrix_Determinant.init(self.n, self.m, self.arr)
        result = Matrix_Determinant.result(self.n, self.arr)
        return result

    def character_value(self):
        '''矩阵特征值'''
        result = Matrix_Character_Value.result(self.n, self.m, self.arr)
        return result
