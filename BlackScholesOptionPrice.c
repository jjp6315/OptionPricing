#include <stdio.h>
#include <math.h>

double compute_d1(double K, double r, double sigma, double S_0, double T);

double N(double x);

int main() {
    double K;
    double r;
    double sigma;
    double T;
    double S_0;

    // Collect input data
    printf("Enter the value of K: ");
    scanf("%lf", &K);
    printf("Enter the value of r: ");
    scanf("%lf", &r);
    printf("Enter the value of sigma: ");
    scanf("%lf", &sigma);
    printf("Enter the value of T: ");
    scanf("%lf", &T);
    printf("Enter the value of S_0: ");
    scanf("%lf", &S_0);
    
    // Calculate d1 and d2
    double d1 = compute_d1(K, r, sigma, S_0, T);
    double d2 = d1 - sigma * sqrt(T);
    
    // Using Black-Scholes equation, calculate the value of C
    double C = S_0 * N(d1) - K * exp(-r * T) * N(d2);
    printf("The value of C is: %lf\n", C);
    // printf("The value of C is: %.2f\n", C);
    }

double compute_d1(double K, double r, double sigma, double S_0, double T){
    return (log(S_0 / K) + (r + pow(sigma, 2.0) / 2.0) * T) / (sigma * sqrt(T));
}

double N(double x){
    return (erf(x / sqrt(2.0)) + 1.0) / 2.0;
}