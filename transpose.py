class Matrix_Transpose:
    def result(n:int,m:int,arr:list):
        arr1 = [[] for i in range(m)]
        for i in range(0, m, 1):
            for j in range(0, n, 1):
                arr1[i].append(arr[j][i])
        return arr1
