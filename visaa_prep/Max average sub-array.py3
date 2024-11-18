def max_average_subarray():
    n,k=map(int,input().split())
    nums=list(map(int,input().split()))
    max_sum=current_sum=sum(nums[:k])
    for i in range(k,n):
        current_sum=current_sum-nums[i-k]+nums[i]
        max_sum=max(max_sum,current_sum)
    max_average=max_sum/k
    print(f"{max_average:.4f}")
max_average_subarray()
