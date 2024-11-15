def is_on_time(X):
    if X>=30:
        return "YES"
    else:
        return "NO"
T=int(input())
for _ in range(T):
    X=int(input())
    result=is_on_time(X)
    print(result)
