#include <stdio.h>
#define bigger_str 100
#define smaller_str 50

int main(){
    char first_str[bigger_str], second_str[smaller_str];
    int i = 0, j = 0;
    printf("\nEnter the first string:\n");
    gets(first_str);
    printf("\nEnter the second string:\n");
    gets(second_str);
    while(first_str[i] != '\0'){
        ++i;
    }
    while(second_str[j] != '\0'){
        first_str[i] = second_str[j];
        ++i;
        ++j;
    }
    first_str[i] = '\0';
    printf("\nFinal form of strings:\n");
    puts(first_str);
    printf("\n");
    return 0;

}