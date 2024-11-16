def win_the_match(x,y):
    return x-y+1
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print(win_the_match(x,y))
