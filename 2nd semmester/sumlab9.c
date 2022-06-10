#include <stdio.h>

int main(){
    int input_array[20], divisible_four[20], divisible_three[20], howManyFour = 0, howManyThree = 0;

    for (int i = 0; i < 20; i++)
    {
        scanf("%d", &input_array[i]);
    }
    for(int i = 0; i < 20; i++)
    {
        if((input_array[i])%4 == 0)
        {
            divisible_four[howManyFour] = input_array[i];
            howManyFour = howManyFour+1;
        }
        if((input_array[i]) % 3 == 0)
        {
            divisible_three[howManyThree] = input_array[i];
            howManyThree = howManyThree + 1;
        }
    }
    for(int i = 0; i < howManyThree; i++)
    {
        printf("%d ", divisible_three[i]);
    }
    printf("\n");
    for(int i = 0; i < howManyFour; i++)
    {
        printf("%d ",divisible_four[i]);
    }
    printf("\n");
    return 0;
}