from log import filelog


class Matrix_Input:
    def flush():
        '''每次调用矩阵输入函数时，先初始化。'''
        Matrix_Input.arr1 = []
        Matrix_Input.arr2 = []
        Matrix_Input.n = 0
        Matrix_Input.m = 0
        Matrix_Input.p = 0
        Matrix_Input.q = 0

    def init(num: int):
        if num == 1:
            Matrix_Input.n, Matrix_Input.m = map(
                int, input("请输入矩阵的行和列：").split())
            Matrix_Input.p = Matrix_Input.n
            Matrix_Input.q = Matrix_Input.m
            filelog("您输入的矩阵为%d行，%d列。" % (Matrix_Input.n, Matrix_Input.m))
        elif num == 2:
            Matrix_Input.n, Matrix_Input.m = map(
                int, input("请输入第一个矩阵的行和列：").split())
            filelog("您输入的第一个矩阵为%d行，%d列。" % (Matrix_Input.n, Matrix_Input.m))
            Matrix_Input.p, Matrix_Input.q = map(
                int, input("请输入第二个矩阵的行和列：").split())
            filelog("您输入的第二个矩阵为%d行，%d列。" % (Matrix_Input.p, Matrix_Input.q))
        elif num == 3 or num == 7 or num == 8:
            Matrix_Input.n, Matrix_Input.m = map(
                int, input("请输入矩阵的行和列：").split())
            while Matrix_Input.n != Matrix_Input.m:
                if num == 3:
                    print("只有方阵才可以求逆，请重新输入。")
                elif num == 7:
                    print("只有方阵才可以求行列式，请重新输入。")
                elif num == 8:
                    print("只有方阵才有特征值，请重新输入。")
                filelog("您输入的不是方阵。")
                Matrix_Input.n, Matrix_Input.m = map(
                    int, input("请输入矩阵的行和列：").split())
            filelog("您输入的矩阵为%d行，%d列。" % (Matrix_Input.n, Matrix_Input.m))
        else:
            Matrix_Input.n, Matrix_Input.m = map(
                int, input("请输入矩阵的行和列：").split())
            filelog("您输入的矩阵为%d行，%d列。" % (Matrix_Input.n, Matrix_Input.m))

    def one():
        print("请输入该矩阵：")
        Matrix_Input.write_in(
            Matrix_Input.arr1, Matrix_Input.n, Matrix_Input.m)
        filelog("矩阵输入完成。")

    def two():
        print("请输入第一个矩阵：")
        filelog("第一个矩阵开始输入。")
        Matrix_Input.write_in(
            Matrix_Input.arr1, Matrix_Input.n, Matrix_Input.m)
        filelog("第一个矩阵输入完成")
        filelog("第二个矩阵开始输入。")
        print("请输入第二个矩阵：")
        Matrix_Input.write_in(
            Matrix_Input.arr2, Matrix_Input.p, Matrix_Input.q)
        filelog("第二个矩阵输入完成。")

    def write_in(arr: list, x: int, y: int):
        for i in range(x):
            arr.append(list(map(int, input().split())))
            while len(arr[i]) != y:
                print("输入有误，请重新输入此行：")
                filelog("您输入的矩阵在第%d行出错" % (i+1))
                del arr[i]
                arr.append(list(map(int, input().split())))
