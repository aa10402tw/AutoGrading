#include <stdio.h>

//int binary_search(/* Write your code here */);

//int main(void){
	/* Write your code here */
//}

//int binary_search(/* Write your code here */){
   /* Write your code here */
//}



int BinarySearch(int x, int data[], int left, int right);

void main(){

  int x=0,size=0;  /* ±ý·j´Mªº¤¸¯À */

  scanf("%d",&size);
  int arr[size];
  for(int i=0;i<size;i++){
    scanf("%d",&arr[i]);
  }
  //for (int i=0;i<size;i++){
  //printf("%d",arr[i]);}

  //printf("Input the searched element: ");
  //scanf("%d", &x);
  //printf("The searched element x is at %d.",binarySearch(x, arr, 0, size)+1);

}

/*int binarySearch(int x, int data[], int left, int right) {
int mid = (left+right)/2;
if (left > right) return -1;
if (x == data[mid]) return mid;
else if (x > data[mid]) return  binarySearch(x ,data, mid+1, right);
else return binarySearch(x, data, left, mid-1);
}
*/
