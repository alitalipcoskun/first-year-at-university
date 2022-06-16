#include<stdio.h>

int main(){

	float top = 0, bottom = 0, left = 0, right = 0, flag = 0;
	scanf("%f %f %f %f", &top, &right, &bottom, &left);
	scanf("%f", &flag);
	float degree[6][8];
	for(int i = 0; i < 8; i++){
		degree[0][i] = top;/*top*/
		degree[5][i] = bottom;/*bottom*/	
	}
	for(int i = 1; i < 5; i++){
		degree[i][0] = left;
		degree[i][7] = right; 	
	}
	for(int i = 1; i < 5; i++){
		for(int j = 1; j < 7; j++){
		degree[i][j] = 0;		
		}	
	}
	printf("\n");
	float update = 0.0, temp = 0.0;
	
	int flag_2 = 1;
	float max;
	while(flag_2){
	max = 0;	
	for(int i = 1; i < 5; i++){
		for(int j = 1; j < 7; j++){
			temp = degree[i][j];
			degree[i][j] = (float)(degree[i-1][j]+degree[i][j-1]+degree[i+1][j]+degree[i][j+1])/(float)4;	
			update = degree[i][j] - temp;
		}
		if(update >= max){
			max = update;		
		}

		}
		if(max < flag){
			flag_2 = 0;	
		}
	}
	printf("Equilibrium values:\n");
	for(int i = 1; i < 5; i++){
		for(int j = 1; j < 7; j++){
			printf("  %.3f", degree[i][j]);		
		}
		printf("\n");	
	}
	 

	return 0;
}
