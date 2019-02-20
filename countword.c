#include <stdio.h>
#include<string.h>
int main() 
{
	char a[100];
	int n,j,count=1;
	scanf("%[^\t\n]s",a);
	n=strlen(a);
	for(j=0;j<n;j++)
	{
	   if(a[j]==' ')
	    {
	        count++;
	    }
	}
	printf("%d",count);
}
