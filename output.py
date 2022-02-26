def output(arr:list):
    '''输出结果'''
    i = len(arr)
    j = len(arr[0])
    for p in range(i):
        for q in range(j):
            print(arr[p][q],end=" ")
        print("")
