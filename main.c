#include <stdio.h>

double add(double a, double b) {
    return a + b;
}

int main() {
    double num1, num2, result;

    scanf("%lf", &num1);
    scanf("%lf", &num2);

    result = add(num1, num2);

    printf("%lf", result);

    return 0;
}
