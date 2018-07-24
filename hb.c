#include<stdio.h>
#include<stdlib.h>
void main()
{
	int m,k=0,i,j,count,x,temp;
	scanf("%d",&m);
	int *a=malloc(sizeof(int)*m);
	int *b=malloc(sizeof(int)*m);
	for(i=0;i<m;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<m;i++)
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
