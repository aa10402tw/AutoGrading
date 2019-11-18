#include <stdio.h>
#include<string.h>
void permute(char *str, int n);

int main(){
  char input[100];
  scanf("%s",input);
  permute(input, strlen(input)) ;

return 0 ;
}

void permute(char *str, int n){
  char ch ;
  int i ;

  if(n==1) {
    printf("%s\n", str) ;
  }
  else {
    for(i=n-1 ; i>=0 ; i--) {
      ch = *(str+i) ;
      *(str+i) = *(str+n-1) ;
      *(str+n-1) = ch ;
      permute(str, n-1) ;
      ch = *(str+i) ;
      *(str+i) = *(str+n-1) ;
      *(str+n-1) = ch ;
    }
  }
}
