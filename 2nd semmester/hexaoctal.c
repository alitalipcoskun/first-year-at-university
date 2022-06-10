#include <stdio.h>

int main(){
    int input;
    char process;
    void decimal_to_binary(int number);
    void decimal_to_octal(int number);
    void decimal_to_hexadecimal(int number);

    

    while(scanf("%d %c", &input, &process) != EOF){
        switch (process)
        {
        case 'b':
            decimal_to_binary(input);
            break;
        case 'B':
            decimal_to_binary(input);
            break;
        case 'o':
            decimal_to_octal(input);
            break;
        case 'O':
            decimal_to_octal(input);
            break;
        case 'h':
            decimal_to_hexadecimal(input);
            break;
        case 'H':
            decimal_to_hexadecimal(input);        
        default:
            break;
        }

    }
}

void decimal_to_binary(int number){
    int binary[100];
    int index = 0;
    while(number != 0){
        binary[index] = number % 2;
        index++;
        number = number / 2;
    }
    int i;
    for(i = index-1; i >= 0; i--){
        printf("%d", binary[i]);
    }
    printf("\n");
}
void decimal_to_octal(int number){
    int octal[100];
    int index = 0;
    while(number != 0){
        octal[index] = number % 8;
        index++;
        number = number / 8;
    }
    int i;
    for(i = index-1; i >= 0; i--){
        printf("%d", octal[i]);
    }
    printf("\n");
}

void decimal_to_hexadecimal(int number){
    int hexadecimal[100];
    int index = 0;
    while(number != 0){
        hexadecimal[index] = number % 16;
        index++;
        number = number / 16;
    }
    int i;
    for(i = index-1; i >= 0; i--){
        if(hexadecimal[i] < 10){
            hexadecimal[i] += 48;
        }
        else{
            hexadecimal[i] += 55;
        }
        printf("%c", hexadecimal[i]);
    }
    printf("\n");
}