N=int(input())
matrix=[]
for i in range(N):
    row=list(map(int,input().split()))
    matrix.append(row)
for i in range(N):
    for j in range(N//2):
        matrix[i][j], matrix[i][N-j-1]=matrix[i][N-j-1],matrix[i][j]
for i in range(N):
    print(*matrix[i])
