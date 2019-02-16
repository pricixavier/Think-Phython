#include <stdio.h>
int main(void) 
{
int a[10],i,n,m=0;
scanf("%d",&n);
for(i=0;i<n;i++)
{
	scanf("%d",&a[i]);
}
for(i=0;i<n;i++)
{
	if(m<a[i])
	{
		m=a[i];
	}
}
printf("%d",m);
}
