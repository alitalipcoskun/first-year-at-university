#include<stdio.h>

int main(){

int input;
scanf("%d", &input);
int i, j;
for(i = 0; i < input; i++){
	printf("  ");
	for(j = 0; j <= i; j++){
	printf("%d   ", j);	
	}
	printf("\n");
}
for(i = input-1; i >= 0; i--){
	if(j != i && i != 0){	
	printf("  ");
	}	
	for(j = 0; j < i; j++){
	printf("%d   ", j);	
	}
	if(j == i && i == 0){
	break;	
	}
	printf("\n");
}
return 0;
}
