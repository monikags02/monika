#include<stdio.h>

#include <stdlib.h>

int main() 
{
    long int a[100000],q,i,j,n=0,t; 
    scanf("%d", &q);
     for(i = 0; i < q; i++)
       scanf("%ld",&a[i]);
	 
	 for (i = 0; i < q-1; i++)      
		for (j = 0; j < q-i-1; j++) 
           if (a[j] < a[j+1])
              {	t =a[j+1];
			  	a[j+1]=a[j];
			  	a[j]=t;
			  }
	for(i = 0; i < q; i++)
    	n=(n*10)+a[i];
    	
    	printf("%ld",n);
}
