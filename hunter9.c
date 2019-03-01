#include <stdio.h>

int main(void) {
					int i,j;
					int n;
					scanf("%d",&n);
					int b[n];
	        for(i=0;i<n;i++)
					{
						scanf("%d",&b[i]);
					}
					for(i=0;i<n;i++)
					{
						for(j=i+1;j<n;j++)
						{
							if(b[i]+b[j]==0)
							{
								printf("%d %d\t",b[i],b[j]);
								break;
							}
						}
					}
	return 0;
}
