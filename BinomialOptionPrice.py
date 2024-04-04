import numpy as np

def binomial_tree_call_option_price(K, r, sigma, T, S, N):
    """
    Binomial Tree Call Option Pricing Model
    Parameters:
    K : float
        Strike price of the option
    r : float
        Annual risk-free interest rate
    T : float
        Time to expiration of the option (in years)
    sigma : float
        Volatility of the underlying asset
    S : float
        Current price of the underlying asset
    N : int
        Number of time steps in the binomial tree

    Returns:
    float
        Call option price
    """

    deltaT = T / N

    u = np.exp(sigma * np.sqrt(deltaT))
    d = 1 / u
    
    p = (np.exp(r * deltaT) - d) / (u - d)

    # Calculate the stock prices at time step N
    stock_prices = np.zeros((N+1, N+1))
    stock_prices[0, 0] = S
    for i in range(1, N+1):
        stock_prices[i, 0] = stock_prices[i-1, 0] * u
        for j in range(1, i+1):
            stock_prices[i, j] = stock_prices[i-1, j-1] * d

    # Initialize matrix and calculate the option values at time step N
    option_values = np.zeros((N+1, N+1))
    option_values[:, -1] = np.maximum(stock_prices[-1] - K, 0)

    # Compute option prices backward recursively
    for j in range(N-1, -1, -1):
        for i in range(j+1):
            option_values[i, j] = np.exp(-r * deltaT) * (p * option_values[i, j+1] + (1 - p) * option_values[i+1, j+1])

    return option_values[0, 0]

def main():
    K = float(input("Enter the value of K: "))
    r = float(input("Enter the value of r: "))
    sigma = float(input("Enter the value of sigma: "))
    T = float(input("Enter the value of T: "))
    S = float(input("Enter the value of S: "))
    N = int(input("Enter the value of N: "))

    call_price = round(binomial_tree_call_option_price(K, r, sigma, T, S, N), 2)
    # call_price = binomial_tree_call_option_price(K, r, sigma, T, S, N)

    print("Binomial Tree Call Option Price:", call_price)


if __name__ == "__main__":
    main()
    
