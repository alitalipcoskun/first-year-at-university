#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int main()
{
    char message[50];
    int number;
    int sum = 0;
    
    printf("Please enter your string: ");
    scanf("%[^\n]", message);//getting string input


    do
    {
        number++;
    } while (message[number] != '\0');

    for(int i = 0; i < number; i++)
    {
        if (message[i] >= 48 && message[i] <= 57)
        {
            char *temp = &message[i];
            int a = atoi(temp);
            sum = sum + a;
        }
    }

    printf("the sum is %d", sum);
    printf("\n\n");

    return 0;
    
}
