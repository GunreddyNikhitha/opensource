def rock_paper_scissors(p1,p2):
    if(p1=='R' and p2=='P') or (p1=='P' and p2=='S') or (p1=='S' and p2=='R'):
        return "Charan"
    elif(p1=='P' and p2=='R') or (p1=='S' and p2=='P') or (p1=='R' and p2=='S'):
        return "Vignesh"
    else:
        return "NULL"
p1,p2=input().split()
winner=rock_paper_scissors(p1,p2)
print(winner)
