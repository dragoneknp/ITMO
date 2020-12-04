#include <stdio.h>
#include <math.h>
#define PI 3.14159265
main()
{
 double a = 0.0;
 scanf("%lf",&a);
 double z1=2*pow((sin((3*PI-2*a)*PI/180)),2)*pow(cos((5*PI+2*a)*PI/180),2); 
 double z2=(1.0/4.0)-(1.0/4.0)*sin((5.0/2.0*PI-8*a)*PI/180); 
 printf("z1=%lf\n",z1); 
 printf("z2=%lf\n",z2); 
 return 0;
