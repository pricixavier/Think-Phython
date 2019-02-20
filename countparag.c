#include <stdio.h>
#include<string.h>
int main(void) {
char ch[100];
int i,j,count=0;
gets(ch);
for(j=0;ch[j]!='\0';++j)
{
	
}
for(i=0;i<j;i++)
{
	if(isdigit(ch[i]))
	count++;
}
printf("%d",count);
}

