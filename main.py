'''
本模块用于调用各种功能函数
'''
from body import Function_Body
from output import output


matrix = Function_Body()
matrix.begin()


def fun():
    if fun_number == 1:
        result = matrix.sum()
        output(result)
    elif fun_number == 2:
        result = matrix.multiple()
        output(result)
    elif fun_number == 3:
        result = matrix.inverse()
        output(result)
    elif fun_number == 4:
        result = matrix.transpose()
        output(result)
    elif fun_number == 5:
        result = matrix.step_shape()
        output(result)
    elif fun_number == 6:
        result = matrix.linear_equation()
        output(result)
    elif fun_number == 7:
        result = matrix.determinant()
        print(result)
    elif fun_number == 8:
        result = matrix.character_value()
        for i in range(len(result)):
            print(result[i][0])

while True:
    fun_number = matrix.target()
    if fun_number == 0:
        exit(0)
    matrix.write(fun_number)
    print("结果为：")
    fun()
