#include <stdio.h>
#include <stdlib.h>

int main()
{
    int in = 0;

    while(1){

        printf("Please enter a number: ");
        scanf("%d", &in);

        if(in == -1) break;

        if(in%2 == 0){
            printf("The number is even.\n");
        }else{
            printf("The number is odd.\n");
        }

    }//end while

    return 0;
}
