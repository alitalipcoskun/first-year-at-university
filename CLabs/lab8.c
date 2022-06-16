#include <stdio.h>
#include <string.h>

int main(){
	char input[50];
	printf("The strings starting with 'Th' are:\n");
	for(int i = 0; i < 5; ++i){	
	scanf("%49s", input);
	int j = 0;
	while(input[j] != '\0'){
		j++;
	}
	//printf("The strings starting with 'Th' are:\n");
	if(input[0] == 'T' && input[1] == 'h'){
	//for(int a = 0; a < j; a++){
		//printf("%c", input[a]);
		printf("%s\n", input);	
	//}
	//printf("\n");*/	
	}
	
	}
	

	return 0;	
}
