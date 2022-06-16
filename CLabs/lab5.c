#include <stdio.h>

int main(){

int first[10], second[10], flag = 0;
for(int i = 0; i < 10; i++){
	scanf(" %d", &first[i]);
}
for(int i = 0; i < 10; i++){
	scanf(" %d", &second[i]);
}

printf(" The First Set: \n");
for(int i = 0; i < 10; i++){
	printf("%d ", first[i]);
}
printf("\n The Second Set: \n");
for(int i = 0; i < 10; i++){
	printf("%d ", second[i]);
}

printf("\n The Union Set: \n");
for(int i = 0; i < 10; i++){
	printf("%d ", first[i]);
}
for(int i = 0; i < 10; i++){
	flag = 0;
	for(int j = 0; j < 10; j++){
		if(second[i] == first[j]){
			flag = 1;
			break;					
		}
	
	}
	if(flag == 0){
		printf("%d ", second[i]);	
	}
}
return 0;
}
