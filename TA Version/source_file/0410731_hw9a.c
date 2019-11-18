#include <stdio.h>

int SUM(int total);

int main(){
	int n;
	scanf("%d",&n);
	SUM(n);
	printf("%d",SUM(n));
	return 0;
}

int SUM(int total){
	if (total==1)
      return 1;
   else
      return SUM(total-1)+total;
}
