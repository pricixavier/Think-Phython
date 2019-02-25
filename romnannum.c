
#include <stdio.h>
#include<string.h>
int main(void) 
{
char s[100];
int w;
scanf("%s",s);
int l=strlen(s);
for(int i=0;i<l;i++)
{
switch(s[i])
{
	case 'I':s[i]=1; break;
	case 'V':s[i]=5; break;
	case 'X':s[i]=10; break;
	case 'L':s[i]=50; break;
	case 'C':s[i]=100; break;
	case 'D':s[i]=500; break;
	case 'M':s[i]=1000; break;
	default:
	printf("invalid");
	break;
}
}
w=s[l-1];
for(int i=l-1;i>=0;i--)
{
	if(s[i]>s[i-1])
	{
		w=w-s[i-1];
	}
	else
	{

		w=w+s[i-1];
	}
}
printf("%d",k);
	return 0;
}
