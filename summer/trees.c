#include <stdio.h>
#include <stdlib.h>

int search(node* tree, int number);

typedef struct node{
    int number;
    struct node *right;
    struct node *left;
}
node;

int main(){

}

int search(node *tree, int number){
    if(tree == NULL){
        return 0;
    }
    else if( number > tree -> number){
        return search(tree->left, number);
    }
    else if(number < tree ->number){
        return search(tree ->right, number);
    }
    else{
        return 1;
    }
}