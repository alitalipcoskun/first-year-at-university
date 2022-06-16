#include <stdio.h>

int main(){

int howMany;
float celcius = 0.0, rankin = 0.0, kelvin = 0.0, fahrenheit= 0.0;
scanf("%d", &howMany);


do{
	fahrenheit = 9*celcius/5 + 32;
	rankin = fahrenheit + 459.67;
	printf("%.2f C   %.2f R\n", celcius, rankin);
	celcius += howMany;


}while(celcius <= 50);

return 0;
}
