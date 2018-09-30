#include <stdio.h>

int main(){
    int n;
    printf("Please input n: ");
    scanf("%d",&n);

    //////未學過迴圈的同學/////
    int f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10;
    f0 = 0;
    f1 = 1;
    f2 = f1 + f0;
    f3 = f2 + f1;
    f4 = f3 + f2;
    f5 = f4 + f3;
    f6 = f5 + f4;
    f7 = f6 + f5;
    f8 = f7 + f6;
    f9 = f8 + f7;
    f10 = f9 + f8;
    if(n == 0)printf("%d", f0);
    else if(n == 1)printf("%d", f1);
    else if(n == 2)printf("%d", f2);
    else if(n == 3)printf("%d", f3);
    else if(n == 4)printf("%d", f4);
    else if(n == 5)printf("%d", f5);
    else if(n == 6)printf("%d", f6);
    else if(n == 7)printf("%d", f7);
    else if(n == 8)printf("%d", f8);
    else if(n == 9)printf("%d", f9);
    else if(n == 10)printf("%d", f10);
    //////未學過迴圈的同學/////


    /*
    //////學過迴圈的同學/////
    int Fn,Fn_1,Fn_2,i;
    Fn_2 = 0;
    Fn_1 = 1;
    i = 2;
    while(i <= n){
        Fn = Fn_1 + Fn_2;
        Fn_2 = Fn_1;
        Fn_1 = Fn;
        i++;
    }
    if(n == 0) Fn = 0;
    else if(n == 1) Fn = 1;
    printf("%d\n",Fn);
    //////學過迴圈的同學/////
    */

    return 0;
}
