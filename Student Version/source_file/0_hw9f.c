#include <stdio.h> 
#include <stdlib.h> 
#include <time.h>

int noConflicts(int *board, int current);
void queens(int *board, int current, int size, unsigned long long *count);
unsigned long long calcQueens(int size);


int main(){ 
    clock_t start, end;
    start = clock();
    int num;
    scanf("%d", &num);
    printf("%llu\n", calcQueens(num));
    end = clock();
    // printf("Total time : %lf\n", (end - start)/(double)(CLOCKS_PER_SEC));
    return 0; 
}

int noConflicts(int *board, int current){
    for(int x=0 ; x<current ; x++){
        if(board[x] == board[current])
            return 0;
        int slash = abs(board[current] - board[x]);
        if(current-x == slash)
            return 0;
    }
    return 1;
}

void queens(int *board, int current, int size, unsigned long long *count){

    if(current == size){
        *count += 1;
        // for(int i=0 ; i<size ; i++)
        //     printf("%d ", board[i]);
        // printf("\n");
    }
    else{
        for(int y=0 ; y<size ; y++){
            // if(current==0)
            //     printf("Calculating if the first Queen is at %d\n", y);
            board[current] = y;
            if(noConflicts(board, current))
                queens(board, current+1, size, count);
        }
    }
}

unsigned long long calcQueens(int size){
    unsigned long long count = 0;
    int board[size];
    for(int i=0 ; i<size ; i++)
        board[i] = -1;
    queens(board, 0, size, &count);
    return count;
}