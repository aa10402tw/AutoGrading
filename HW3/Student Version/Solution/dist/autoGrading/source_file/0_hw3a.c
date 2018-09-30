#include <stdio.h>

int main(){
    int a1, a2, b1, b2;
    float Dist;
    printf("Please input Point A and Point B: ");
    scanf("A(%d,%d) B(%d,%d)", &a1,&a2,&b1,&b2);

    printf("Please input Dist: ");
    scanf("%f", &Dist);

    float A_B_DIst_pow2 = (a1 - b1)*(a1 - b1) + (a2 - b2)*(a2 - b2);
    float Dist_pow2 = Dist*Dist;
    if(A_B_DIst_pow2 > Dist_pow2) printf(">");
    else if(A_B_DIst_pow2 == Dist_pow2) printf("=");
    else printf("<");

    return 0;
}
