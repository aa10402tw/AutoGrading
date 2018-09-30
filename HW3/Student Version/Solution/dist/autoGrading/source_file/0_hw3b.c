#include <stdio.h>

int main(){
    int d0, d1, d2, d3, d4, d5, d6, d7, d8, d9;
    int sum;
    printf("Please input n: ");
    scanf("%1d%1d%1d%1d%1d%1d%1d%1d%1d%1d", &d9,&d8,&d7,&d6,&d5,&d4,&d3,&d2,&d1,&d0);

    sum = d9 - d8 + d7 - d6 + d5 - d4 + d3 - d2 + d1 - d0;
    printf("%1d - %1d + %1d - %1d + %1d - %1d + %1d - %1d + %1d - %1d = %d", d9,d8,d7,d6,d5,d4,d3,d2,d1,d0,sum);

    return 0;
}
