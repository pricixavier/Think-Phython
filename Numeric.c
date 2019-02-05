//numeric
#include <stdio.h>
 
int main(void) {
	char string[10];
	int len,i;
	scanf("%s",string);
	len=strlen(string);
	for(i=0;i<len;i++)
	{
		if(string[i]>='0' && string[i]<='9')
		{
			printf("yes");
		}
		else
			printf("no");
			break;
 
	}
	return 0;
}
