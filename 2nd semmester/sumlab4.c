#include <stdio.h>

int main(){
    int input;
    int howMany[10];   
     for(int i = 0; i <= 9; i++)
    {
        howMany[i] = 0;
    }
    while(scanf("%i", &input) != EOF)
    {   

        switch (input)
        {
        case '0':
            howMany[0]++;
            break;
        case '1':
            howMany[1]++;
            break;
        case '2':
            howMany[2]++;
            break;
        case '3':
            howMany[3]++;
            break;
        case '4':
            howMany[4]++;
            break;
        case '5':
            howMany[5]++;
            break;
        case '6':
            howMany[6]++;
            break;
        case '7':
            howMany[7]++;
            break;
        case '8':
            howMany[8]++;
            break;
        case '9':
            howMany[9]++;
            break;

        
        default:
            break;
        }
        for(int i = 0; i <= 9; i++)
        {
            printf("%d", i);
            for (int j = 0; j < howMany[i]; j++)
            {
                printf("*");
            }
            printf("\n");
        }
        printf("\n");
        return 0;
    }
}