from log import filelog


class Matrix_Sum:
    '''当只需要调用类的函数，不需要实例化的时候，每个函数前面可以不写self'''
    def result(n,m,arr1,arr2):
        arr3 = [[] for i in range(n)]
        for i in range(n):
            for j in range(m):
                arr3[i].append(arr1[i][j] + arr2[i][j])
        filelog("矩阵运算完成。")
        return arr3