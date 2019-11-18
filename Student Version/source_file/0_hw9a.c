#include <stdio.h>

int SUM(int N);

int main(){
	int N;
	scanf("%d", &N);
	printf("%d\n", SUM(N));
	return 0;
}

int SUM(int N){
	if(N==1)
		return 1;
	else
		return N+SUM(N-1);
}