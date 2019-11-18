#include <stdio.h>
#include<math.h>

void hanoi(double num, char x, char y, char z);

int main() {
    double n=0,sum=0;
    scanf("%lf", &n);
    //hanoi(n, 'x', 'y', 'z');
    sum=pow(2,n);
    printf("%.lf",sum-1);
}

void hanoi(double num, char x, char y, char z){
        hanoi(num-1, x, z, y);
        hanoi(1, x, y, z);
        hanoi(num-1, y, x, z);
}



