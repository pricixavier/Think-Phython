#include<stdio.h>
int main(void)
{
	int b[1000];
	int i,j,n,k;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		scanf("%d",&b[i]);
	}
	for(i=1;i<=n;i++)
	{
		for(j=i+1;j<=n;j++)
		{
			for(k=i+2;k<=n;k++)
			{
			if(b[i]+b[j]==b[k])
			{
				printf("%d %d %d\n",b[i],b[j],b[k]);
			}
			}

		}
	}
	return 0;
}
