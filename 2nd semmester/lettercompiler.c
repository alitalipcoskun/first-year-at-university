#include <stdio.h>

char letter_compiler(char letter)
{
    if ( (int)letter <= 123 && (int)letter >= 97)
    {
        letter = letter - 32; 
    } 
    return (char)letter;
}


int main()
{
    char letter, bigger_letter;

    printf("Please enter an letter: ");
    scanf("%c", &letter);
    printf("%d\n", letter);

    char finale = letter_compiler(letter);

    printf("%c\n\n", finale);


}