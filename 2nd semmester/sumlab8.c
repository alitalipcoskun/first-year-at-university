#include <stdio.h>
void plural(char *s1, char *s2);
int main()
{
    char string1[80], string2[80];
    printf("Enter a noun\n");
    scanf("%s",string1);

	plural(string1,string2);
    printf("%s %s\n",string1,string2);
    return 0;
}

void plural(char *s1, char *s2){
    int length = 0;
    for(int i = 0; i <80; i++)
    {
        if(s1[i] == '\0')
        {
            length = i;
            break;
        }
    }
    for(int i = 0; i < length; i++)
    {
        s2[i] = s1[i];
    }
    if(s1[length-1] == 'y')
    {
        s2[length-1] = 'i';
        s2[length] = 'e';
        s2[length+1] = 's';
        s2[length+2] = '\0';
    }
    else if((s1[length-1] == 'y') || ((s1[length-2] == 's' || s1[length-2] == 'c') && s1[length-1] == 'h'))
    {
        s2[length] = 'e';
        s2[length+1] = 's';
        s2[length+2] = '\0';
    }
    else{
        s2[length] = 's';
        s2[length+1] = '\0';
    }
}