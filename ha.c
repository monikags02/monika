#include<stdio.h>
#include<stdlib.h>
void main()
{
	int n,k=0,i,j,count,x,temp;
	scanf("%d",&n);
	int *a=malloc(sizeof(int)*n);
	int *b=malloc(sizeof(int)*n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<n;i++)
	{
		if(a[i]==i)
		{
			b[k]=a[i];
			k++;
		}
	}
	if(k==0)
	{
		printf("-1");
	}
	else
	{
		for(i=0;i<k;i++)
		{
			printf("%d\t",b[i]);
		}
	}
}
