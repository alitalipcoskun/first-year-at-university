#include <stdio.h>
#include <string.h>

int main(){
    char str[100], temp;
    printf("\nEnter the string:\n");
    gets(str);
    int i = 0, j = strlen(str)-1;//because of'\0 character;
    while(i < j){
        temp = str[j];
        str[j] = str[i];
        str[i] = temp;
        j--;
        i++;
    }
    printf("\nThe reversed string is:\n");
    puts(str);
    printf("\n");
    return 0;
}