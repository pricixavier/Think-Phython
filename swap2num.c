#include <stdio.h>

int main(void) {
	int c,d,t;
	scanf("%d%d",&c,&d);
	t=d;
	d=c;
	c=t;
	printf("%d %d",c,d);
	
}
