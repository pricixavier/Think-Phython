#include <stdio.h>

int main(void) {
	long int a,n,d,s=0;
	scanf("%ld %ld %ld",&n,&a,&d);
            s = (n * (2 * a + (n - 1)* d ))/ 2;
	printf("%ld",s);
	return 0;
}
