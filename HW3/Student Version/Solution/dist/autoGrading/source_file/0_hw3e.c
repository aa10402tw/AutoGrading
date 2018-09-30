#include <stdio.h>

int main(){
    int a, b, c, d;
    int Ans;
    printf("Please input a b c d: ");
    scanf("%d %d %d %d",&a,&b,&c,&d);

    Ans = a + b * c - d;
    printf("%d", Ans);

    return 0;
}
