#include <stdio.h>

int permutate(int a, int b);

int main(){
    int objects, times, result;
    scanf("%d %d", &objects, &times);
    times = objects - times;
    result = permutate(objects, times);
    printf("%d\n", result);
    return 0;
}
int permutate(int a, int b){
    if(a == b){
        return 1;
    }
    else{
        return a * permutate(a-1, b);
    }
}