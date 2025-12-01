import math
from scipy.stats import norm

# --- Black-Scholes-Merton Function ---

def black_scholes_merton(S, K, T, r, sigma):
    """
    Calculates the theoretical price of a European Call and Put option
    using the Black-Scholes-Merton model.

    Args:
        S (float): Current stock price (Spot Price).
        K (float): Option strike price.
        T (float): Time to expiration (in years, e.g., 0.5 for six months).
        r (float): Risk-free interest rate (annualized, decimal, e.g., 0.05).
        sigma (float): Volatility of the underlying stock (annualized, decimal, e.g., 0.30).

    Returns:
        tuple: (call_price, put_price)
    """
    if T <= 0:
        # Handle the case where time to maturity is zero or negative
        if S > K:
            call_price = S - K
            put_price = 0.0
        else:
            call_price = 0.0
            put_price = K - S
        return call_price, put_price

    # 1. Calculate d1 and d2
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    # 2. Calculate N(d1), N(d2), N(-d1), N(-d2)
    # N(x) is the cumulative distribution function (CDF) of the standard normal distribution
    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)
    N_neg_d1 = norm.cdf(-d1)
    N_neg_d2 = norm.cdf(-d2)

    # 3. Calculate Call and Put Prices
    # Call Price: C = S * N(d1) - K * exp(-rT) * N(d2)
    call_price = S * Nd1 - K * math.exp(-r * T) * Nd2

    # Put Price: P = K * exp(-rT) * N(-d2) - S * N(-d1)
    put_price = K * math.exp(-r * T) * N_neg_d2 - S * N_neg_d1

    return call_price, put_price

# --- User Input and Execution ---

def get_user_input(prompt, value_type=float, min_val=0.0):
    """
    Utility function to safely get and validate numerical user input.
    """
    while True:
        try:
            value = value_type(input(prompt))
            if value < min_val:
                print(f"Error: Value must be at least {min_val}.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

def main():
    """
    Main function to handle user interaction and output the results.
    """
    print("\n--- Black-Scholes-Merton European Option Pricer ---")
    print("Please enter the required parameters.")

    # Get Inputs
    S = get_user_input("Current Stock Price (S): $")
    K = get_user_input("Option Strike Price (K): $")
    T = get_user_input("Time to Expiration (T, in years, e.g., 0.5): ", min_val=0.0001) # Avoid T=0 for log/sqrt
    r = get_user_input("Risk-Free Rate (r, decimal, e.g., 0.05 for 5%): ", min_val=-0.5) # Allow slightly negative rates
    sigma = get_user_input("Volatility (sigma, decimal, e.g., 0.30 for 30%): ", min_val=0.0001)

    # Calculate Prices
    call_price, put_price = black_scholes_merton(S, K, T, r, sigma)

    # Output Results
    print("\n--- Results ---")
    print(f"Input Parameters:")
    print(f"  Spot Price (S):      ${S:.2f}")
    print(f"  Strike Price (K):    ${K:.2f}")
    print(f"  Time (T):            {T:.4f} years")
    print(f"  Risk-Free Rate (r):  {r:.4f}")
    print(f"  Volatility (sigma):  {sigma:.4f}")
    print("-" * 25)
    print(f"European Call Price: ${call_price:.4f}")
    print(f"European Put Price:  ${put_price:.4f}")
    print("-" * 25)

if __name__ == "__main__":
    # Ensure scipy is installed (e.g., pip install scipy)
    main()