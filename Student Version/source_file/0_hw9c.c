#include <stdio.h> 

void swap(int *i, int *j);
int binary_search(int arr[], int left, int right, int target);
void selection_sort(int *tmp_arr, int num);


int main(void){ 
	int num, target;
	scanf("%d", &num);
	int arr[num];
	for(int i=0 ; i<num ; i++)
		scanf("%d", &arr[i]);
	scanf("%d", &target);
	selection_sort(arr, num);
	printf("%d\n", binary_search(arr, 0, num-1, target));
	return 0; 
}

void swap(int *i, int *j){
	int tmp = *i;
	*i = *j;
	*j = tmp;
}

int binary_search(int arr[], int left, int right, int target){ 
   if (right >= left) 
   { 
        int mid = left + (right - left)/2; 
  
        // If the element is at the middle, return itself
        if (arr[mid] == target)   
            return mid; 
  
        // If than element is smaller than mid, search the left part
        if (arr[mid] > target)  
            return binary_search(arr, left, mid-1, target); 
  
        // Else the element can only be at the right part
        return binary_search(arr, mid+1, right, target); 
   } 
  
   // When the element is not in the array
   return -1; 
} 

void selection_sort(int *tmp_arr, int num){
	for(int i=0 ; i<num ; i++){
		int min = i;
		for(int j=i+1 ; j<num ; j++){
			if(*(tmp_arr+j) < *(tmp_arr+min))
				min = j;
		}
		if(i!= min)
			swap(tmp_arr+i, tmp_arr+min);
	}
}
