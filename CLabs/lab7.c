#include<stdio.h>

void pointer(int samplemax[],int samplemin[], int size, int *p1, int *p2){

//fill that function
	int maximum = samplemax[0], minimum = samplemin[0];
	for(int i = 0; i < size;++i){
	if(p1[i] >= maximum){
	maximum = p1[i];	
	p1[0] = p1[i];
	}
	if(p2[i] <= minimum){
	minimum = p2[i];
	p2[0] = p2[i];
	}
	}


}

int main(){
	int *p1,*p2;				//do not change
	int howMany;

	scanf("%d", &howMany);
	// fill this space
	int maxarr[howMany];
	p1 = &maxarr[0];
	for(int i = 0; i < howMany; ++i){
		scanf("%d", &maxarr[i]);
	}
	int minarr[howMany];
	p2 = &minarr[0];
	for(int i = 0; i < howMany; ++i){
		minarr[i] = maxarr[i];
	}
	
	pointer(maxarr, minarr, howMany, p1, p2);

	printf("*p1= %d\n",*p1);	//do not change
	printf("*p2= %d\n",*p2);	//do not change

}
