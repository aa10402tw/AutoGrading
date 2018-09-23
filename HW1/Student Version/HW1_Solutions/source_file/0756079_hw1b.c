#include <stdio.h>
#include <stdlib.h>

int main()
{
    float celsius;

    printf("Please enter a Celsius temperature: ");

    scanf("%f", &celsius);

    float fahrenheit = (celsius * (9.0f/5)) + 32;

    printf("Fahrenheit temperature is %.2f.", fahrenheit);

    return 0;
}
