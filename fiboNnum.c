#include <stdio.h>
int main(void) {
int j, n, a1 = 1, a2 = 1, n1;
scanf("%d", &n);
for (j = 1; j <= n; ++j)
    {
        printf("%d ", a1);
        n1 = a1 + a2;
        a1 = a2;
        a2 = n1;
    }

}
