T = int(input())
for testcases in range(T):
    N = int(input())
    arr = list(map(int, input().strip().split()))
    EVEN=[]
    ODD=[]
    for i in range(0,len(arr),2):
        EVEN.append(arr[i])
    for j in range(1,len(arr),2):
        ODD.append(arr[j])
    sum_of_even=sum(EVEN)
    sum_of_odd=sum(ODD)
    if sum_of_odd>sum_of_even:
        print(sum_of_odd)
    else:
        print(sum_of_even)