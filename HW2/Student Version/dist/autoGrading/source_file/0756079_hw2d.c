#include <stdio.h>
#include <stdlib.h>

int main()
{

    char in_char;

    printf("Please enter a char: ");
    scanf("%c", &in_char);

    printf("your char is '%c', it ASCII code is %d.", in_char, (int)in_char);

    return 0;
}
