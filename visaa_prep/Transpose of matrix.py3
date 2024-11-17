n=int(input())
matrix=[]
for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
for i in range(n):
    for j in range(n):
        print(matrix[j][i], end=" ")
    print()
