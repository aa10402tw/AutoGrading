#include <stdio.h>

void hanoi(int n, char from, char rest, char dest, int *count);

int main() {
    int n, count=0;
    scanf("%d", &n);
    hanoi(n, 'A', 'B', 'C', &count);
    printf("%d\n", count);
    return 0;
} 

void hanoi(int n, char from, char rest, char dest, int *count){
    if(n == 1) {
        *count += 1;
        // printf("Move sheet from %c to %c\n", from, dest);
    }
    else {
        hanoi(n-1, from, dest, rest, count);
        hanoi(1, from, rest, dest, count);
        hanoi(n-1, rest, from, dest, count);
    }
}