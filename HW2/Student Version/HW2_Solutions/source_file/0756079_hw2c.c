#include <stdio.h>
#include <stdlib.h>

int main()
{
    int year;
    int month;
    int day;

    printf("Please enter a data (format: mm/dd/yyyy): ");
    scanf("%d/%d/%d", &month, &day, &year);

    printf("your input data is %04d%02d%02d.", year, month, day);

    return 0;
}
