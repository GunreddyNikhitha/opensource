def max_mangoes(x,y,z):
    max_mango_weight=z-y
    max_mangoes=max_mango_weight//x
    return max_mangoes
x,y,z=map(int,input().split())
result=max_mangoes(x,y,z)
print(result)
