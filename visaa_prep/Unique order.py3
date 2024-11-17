def unique_elements(n,arr):
    unique_elements=[]
    for element in arr:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements
n=int(input())
arr=list(map(int,input().split()))
unique_elements=unique_elements(n,arr)
print(*unique_elements)
