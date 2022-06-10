#include <stdio.h>
#include <math.h>

/*enum day{sun,mon,tues,weds,thurs,fri,sat};
    enum day today = fri;
    sun == 0;
    mon == 1
    .
    .
    .


    #include <library.h>
    #include FILE
    e.g myfile.h

    #define macro facility

    #define C 299792.459
    #define EQ == 

    #define  SQ(x) ((x)*(x))
    
    sat == 6*/

enum day{sun,mon,tues,weds,thurs,fri,sat}; // declare type.

void print_day(enum day d)
{
    switch(d)
    {
        case sun: printf("Sunday.\n"); break;
        case mon: printf("Monday.\n"); break;  
        case tues: printf("Tuesday.\n"); break;
        case weds: printf("Wednesday.\n"); break;
        case thurs: printf("Thursday.\n"); break;
        case fri: printf("Friday.\n"); break;
        case sat: printf("Saturday.\n"); break;
        default: printf("%d is an error.\n", d);
    }
}

enum day next_day(enum day d)
{
    return ((d + 1) % 7);
}


int main()
{
    enum day today = fri;
    print_day(today);
    printf("\n\n");
    print_day(7);
    printf("\n\n");
    print_day(next_day(today));
    printf("\n\n");

    return 0;
}