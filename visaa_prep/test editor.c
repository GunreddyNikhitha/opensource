#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int N,X,Y;
    scanf("%d%d%d",&N,&X,&Y);
    if(Y%X==0 && Y<=N*X){
        printf("YES");
    } else{
        printf("NO");
    }
    return 0;
}
