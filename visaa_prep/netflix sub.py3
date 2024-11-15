#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int a,b,c,x;
    scanf("%d%d%d%d", &a,&b,&c,&x);
    if(a+b>=x || a+c>=x ||b+c>=x){
        printf("YES\n");
    } else {
        printf("NO\n");
    }
    return 0;
}
