def balance_array(A):
    N=len(A)
    B=[0]*N
    for i in range(N):
        left_weight=sum(A[:i])
        right_weight=sum(A[i + 1:])
        B[i]=abs(left_weight - right_weight)
    return B
N=int(input())
A=list(map(int,input().split()))
B=balance_array(A)
print(*B)
