from log import filelog


class Matrix_Determinant:
    def init(n,m,arr):
        Matrix_Determinant.n = n
        Matrix_Determinant.m = m
        Matrix_Determinant.arr = arr
        Matrix_Determinant.line = []
        Matrix_Determinant.array = []
        for i in range(n):
            Matrix_Determinant.array.append(i)

    def arrangement(arr,position,end):
        if position == end:
            Matrix_Determinant.line.append(arr[:])
        else:
            for index in range(position,end):
                arr[index], arr[position] = arr[position], arr[index]
                Matrix_Determinant.arrangement(Matrix_Determinant.array,position+1,end)
                arr[index], arr[position] = arr[position], arr[index]
    
    def result(n,arr):
        Matrix_Determinant.arrangement(Matrix_Determinant.array,0,n)
        index = 0  #指数
        temp = 1
        sum = 0
        for i in range(len(Matrix_Determinant.line)):
            for j in range(0,n-1,1):
                for k in range(j+1,n,1):
                    if Matrix_Determinant.line[i][j]>Matrix_Determinant.line[i][k]:
                        index+=1
            for p in range(n):
                    temp *= arr[p][Matrix_Determinant.line[i][p]]
            if index%2 == 0:
                sum += temp
            else:
                sum -= temp
            index = 0
            temp=1
        filelog("行列式求解完成。")
        return sum