#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("char's memory size: %d byte\t\r\n", sizeof(char));
    printf("short's memory size: %d bytes\n", sizeof(short));
    printf("int's memory size: %d bytes\n", sizeof(int));
    printf("float's memory size: %d bytes\n", sizeof(float));
    printf("double's memory size: %d bytes", sizeof(double));

    return 0;
}