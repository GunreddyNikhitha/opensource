def has_pair_with_sum(arr,k):
    seen=set()
    for num in arr:
        if k - num in seen:
            return True
        seen.add(num)
    return False
N=int(input())
arr=list(map(int,input().split()))
k=int(input())
if has_pair_with_sum(arr,k):
    print("true")
else:
    print("false")
