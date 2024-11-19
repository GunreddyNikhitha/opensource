n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
zero_rows=set()
zero_columns=set()
for i in range(n):
    for j in range(m):
        if grid[i][j]==0:
            zero_rows.add(i)
            zero_columns.add(j)
for i in range(n):
    for j in range(m):
        if i in zero_rows or j in zero_columns:
            grid[i][j]=0
for row in grid:
    print(" ".join(map(str, row)))
