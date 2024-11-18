from collections import Counter
n=int(input())
arr=list(map(int,input().split()))
freq=Counter(arr)
sorted_arr=sorted(arr, key=lambda x: (freq[x], -x))
print(" ".join(map(str, sorted_arr)))
