#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

char* copy(char *str, int size);
void printer_of_string(char *str, int size);
void getting_string(char* str, int size);


int main(){
    char *inputString, *outputString;
    int lengthOfString;
    scanf("%d", &lengthOfString); // We took input from user in order to use in MALLOC func.
    inputString =(char*)malloc(sizeof(char) * lengthOfString+1); // We add 1 because of null character (\0)
    getting_string(inputString, lengthOfString);
    //COPYING A STRING TO ANOTHER POINTER
    outputString = copy(inputString, lengthOfString);
    printer_of_string(outputString, lengthOfString);
    free(inputString);
    free(outputString);
    return 0;
}

void getting_string(char* str, int size){
    for(int i = 0; i < size; ++i){
        scanf("%c", &str[i]);
    }
}

void printer_of_string(char *str, int size){
    for(int i = 0; i < size; ++i){
        printf("%c", str[i]);
    }
    printf("\n");
}

char* copy(char *str, int size){
    char *copy;
    copy = (char*)malloc(sizeof(char)*size+1);
    for(int i = 0; i < size; ++i){
        copy[i] = str[i];
    }
    return copy;
}