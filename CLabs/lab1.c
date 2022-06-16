#include <stdio.h>

int main(){
float grade;
scanf("%f", &grade);
if(grade < 1.0 && grade >= 0.0){
printf("Failed semester--registration suspended\n");
}
else if(grade < 2.0 && grade >= 1.0){
printf("On probation for next semester\n");
}
else if(grade < 3.50 && grade >= 3.0){
printf("Dean's list for semester\n");
}
else if(grade <= 4.0 && grade >= 3.50){
printf("Highest honors for semester\n");
}
return 0;
}
