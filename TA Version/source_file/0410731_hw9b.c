#include <stdio.h>

int GCD(int num1,int num2);

int main(){
   int a=0,b=0;
   scanf("%d %d",&a,&b);
   GCD(a,b);
   printf("%d",GCD(a,b));
   return 0;
}

int GCD(int num1,int num2){
    if(num2 == 0)
        return num1;
    else
        return GCD(num2, num1 % num2);
}
