def min_planes(x,n):
    planes_need=(n+99) // 100
    planes_to_purchase=planes_need-x
    return planes_to_purchase
x,n=map(int,input().split())
print(min_planes(x,n))
