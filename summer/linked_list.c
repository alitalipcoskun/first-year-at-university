/*Linked Lists*/

#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;



int main(){
    node *n, *list;
    list = NULL;//beginning of the story. 
    n = malloc(sizeof(node));
    if(n == NULL){
        return 1;
    }
    n -> number = 1;
    n -> next = NULL;
    list = n;
    n = malloc(sizeof(node));
    if(n== NULL){// security
        free(list);// for not letting leak the memory
        return 1;
    }
    n -> number = 2;
    n -> next = NULL;
    list->next = n;
    n = malloc(sizeof(node));
    if(n == NULL){
        free(list -> next);
        free(list);
        return 1;
    }
    n -> number = 3;
    n -> next = NULL;
    list -> next -> next = n;
    for(node *tmp = list; tmp != NULL; tmp = tmp->next){
        printf("%d\n", tmp->number);
    }
    int input;
    scanf("%d", &input);
    n = malloc(sizeof(node));
    if(n == NULL){
        while( list != NULL){// getting rid of memories after using nodes.
        node *tmp = list -> next;
        free(list);
        list = tmp;
        }   
        return 1;
    }
    n -> number = input;
    n -> next = list;
    list = n;
    printf("\n\n");
    for(node *tmp = list; tmp != NULL; tmp = tmp->next){
        printf("%d\n", tmp->number);
    }
    while( list != NULL){// getting rid of memories after using nodes.
        node *tmp = list -> next;
        free(list);
        list = tmp;
    }
}