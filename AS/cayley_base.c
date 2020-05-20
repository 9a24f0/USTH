#include <stdio.h>

int main () {
    int n;
    scanf("%d", &n);
    printf("\n\n");
    int i, j;
    for(j = 0; j < n; j++) {
        printf("%d\t", j);
        if(j == 0) printf("|\t");
    }
    printf("\n");
    for(i = 0; i <= 8 * n; i++) {
        printf("-");
    }
    printf("\n");
    for(j = 1; j < n; j++) {
        printf("%d\t|", j);
        for(i = 1; i < n; i++) {
            printf("\t%d", (i * j) % n);
        }
        printf("\n");
    }

    return 0;
}