#include <stdio.h>

int main(){
    int d0, d1, d2, d3, d4, d5, d6, d7, d8;
    unsigned int sum;
    printf("Please input n: ");
    scanf("%1d%1d%1d%1d%1d%1d%1d%1d%1d",&d8,&d7,&d6,&d5,&d4,&d3,&d2,&d1,&d0);

    sum = (((((((d0*10+d1)*10+d2)*10+d3)*10+d4)*10+d5)*10+d6)*10+d7)*10+d8;
    //printf("((((((((%d*10+%d)*10+%d)*10+%d)*10+%d)*10+%d)*10+%d)*10+%d)*10+%d = %d", d0,d1,d2,d3,d4,d5,d6,d7,d8,sum);
    printf("%d", sum);

    return 0;
}
