from log import filelog


class Matrix_Multiple:
    '''矩阵的乘法'''
    def result(n,q,m,arr1,arr2):
        temp = 0
        arr3 = [[] for i in range(n)]
        for i in range(n):
            for j in range(q):
                for x in range(m):
                    temp = temp + arr1[i][x] * arr2[x][j]
                arr3[i].append(temp)
                temp = 0
        filelog("矩阵运算完成。")
        return arr3
