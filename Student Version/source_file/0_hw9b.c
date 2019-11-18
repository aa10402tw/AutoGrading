#include <stdio.h>

int GCD(int n1, int n2);

int main()
{
   int n1, n2;
   scanf("%d %d", &n1, &n2);
   printf("%d", GCD(n1,n2));
   return 0;
}

int GCD(int n1, int n2){
    if (n2 != 0)
       return GCD(n2, n1%n2);
    else 
       return n1;
}