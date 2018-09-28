#include <stdio.h>
#include <stdlib.h>

int main()
{
    char in;

    printf("Please enter a char: ");

    scanf("%c", &in);

    int assii = (int)in;
    if((assii >= 97) && (assii <= 122)){
        assii -= 32;
    }

    printf("The uppercase char is %c.", (char)assii);

    return 0;
}
