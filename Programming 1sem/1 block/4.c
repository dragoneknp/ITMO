#include <stdio.h>
#include <math.h>
main(){
 int c; 
 int a; 
 scanf("%d",&a); 
 c= (a>=21) && (a<=45); 
 printf("Результат = %d\n",c);
 printf("---------------------\n");
 int r; 
 scanf("%d",&r); 
 printf("%d",(r >> 16)%2); 
 return 0;

}
