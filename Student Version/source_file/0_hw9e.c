#include <stdio.h>
#include <string.h>
#define input_len 9

int fac(int n);
void swap(char *x, char *y);
void permute(char *str_arr, char *res, int left, int right, int *row);

/* Driver program to test above functions */
int main(){ 
    int n=0;  // Inital legth of input string
    int row=0;  // 
    char str[input_len]; // Initial string
    scanf("%s", str);

    // Calculate the length of input string
    for(int i=0 ; str[i]!='\0' ; i++)
        n++;

    int size = fac(n);
    char res[size][input_len];  // Result after permutation

    // Permutation
    permute(str, res, 0, n-1, &row);

    // Selection sort for res, 
    for(int i=0 ; i<row ; i++){
        int min = i;
        for(int j=i+1 ; j<row ; j++){
            if(strcmp(res[j], res[min])<0)
                min = j;
        }
        if(i!= min){
            char tmp[input_len];
            strcpy(tmp, res[i]);
            strcpy(res[i], res[min]);
            strcpy(res[min], tmp);
        }
    }

    for(int i=0 ; i<row ; i++){
        printf("%s", res[i]);
        printf("\n");
    }
    return 0; 
} 

int fac(int n){
    if(n==2)
        return 2;
    else
        return n*fac(n-1);
}

void swap(char *x, char *y){ 
    char tmp; 
    tmp = *x; 
    *x = *y; 
    *y = tmp;
}

void permute(char *str_arr, char *res, int left, int right, int *row){  
    if (left == right) {
        strcpy(res+(*row)*input_len, str_arr);
        *row += 1;
    }
    else{ 
        for (int i = left; i <= right; i++){ 
            swap((str_arr+left), (str_arr+i)); 
            permute(str_arr, res, left+1, right, row); 
            swap((str_arr+left), (str_arr+i)); //backtrack 
        } 
    }
} 