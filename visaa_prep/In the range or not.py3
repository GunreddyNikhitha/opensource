def can_hear(freq):
    return 67<= freq <=45000
t=int(input())
for _ in range(t):
    X=int(input())
    if can_hear(X):
        print("YES")
    else:
        print("NO")
