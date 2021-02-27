#include <stdio.h>
int main() {
    int i, n, first_term = 0, second_term = 1, nextTerm;
    printf("Enter the number of terms: ");
    scanf("%d", &n);
    printf("Fibonacci Series: ");

    for (i = 1; i <= n; ++i) {
        printf("%d, ", first_term);
        nextTerm = first_term + second_term;
        first_term = second_term;
        second_term = nextTerm;
    }

    return 0;
}

void dead_fn() {
    printf('C program');
}