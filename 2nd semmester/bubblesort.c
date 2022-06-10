#include <stdio.h>
#define SIZE 10

void bubleSort(int *const array, const size_t size);


int main(void){
    int a [SIZE] = {2,6,31,5,10,22,1,33,13,29};

    puts("Data items in original order");
    for(int i = 0; i < SIZE; ++i){
        printf("%4d", a[i]);
    }
    printf("\n");
    bubleSort(a, SIZE);
    puts("Data items in ascending order");
    for(int i = 0; i < SIZE; ++i){
        printf("%4d", a[i]);
    }
    printf("\n");
    return 0;

}

void bubleSort(int * const array, const size_t size){
    void swap(int *element1Ptr, int *element2Ptr);

    for(unsigned int pass = 0; pass < size-1; ++pass){

        for(size_t i = 0; i < size-1; ++i){
            if(array[i] > array[i+1]){
                swap(&array[i], &array[i+1]);
            }
        }
    }
}

void swap(int *element1Ptr, int *element2Ptr){
    int temp;
    temp = *element1Ptr;
    *element1Ptr =  *element2Ptr;
    *element2Ptr = temp;
}