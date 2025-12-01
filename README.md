Black-Scholes-Merton European Option Pricer

This is a simple command-line utility written in Python that calculates the theoretical fair value of a European Call and Put option using the Black-Scholes-Merton (BSM) model.

🌟 Features

Calculates both Call and Put option prices simultaneously.

Handles user input validation to ensure positive values for critical parameters (Spot Price, Strike Price, Volatility).

Correctly implements the core BSM formulas using mathematical and statistical functions.

🛠️ Requirements

This script requires Python 3.x and the following external library:

SciPy: Used for the cumulative distribution function (CDF) of the standard normal distribution, which is denoted as $N(d_1)$ and $N(d_2)$ in the formula.

You can install the required library using pip:

pip install scipy


🚀 Usage

Save the script: Save the provided code as bsm_option_pricer.py.

Run from terminal: Execute the script using Python.

python bsm_option_pricer.py


Enter Parameters: The script will prompt you to input the five required parameters:

Parameter

Variable

Description

Example Input

Current Stock Price

S

The current market price of the underlying asset.

100.00

Option Strike Price

K

The price at which the option holder can buy (Call) or sell (Put).

105.00

Time to Expiration

T

The time remaining until expiration, expressed in years.

0.5 (6 months)

Risk-Free Rate

r

The annualized risk-free interest rate (e.g., T-bill rate), in decimal form.

0.05 (5%)

Volatility

$\sigma$ (sigma)

The annualized standard deviation of the underlying asset's returns, in decimal form.

0.30 (30%)

📐 The Black-Scholes-Merton Formula

The BSM model provides the theoretical price for a European option.

Call Option Price ($C$)

$$C = S N(d_1) - K e^{-rT} N(d_2)$$

Put Option Price ($P$)

$$P = K e^{-rT} N(-d_2) - S N(-d_1)$$

Where:

$S$: Spot Price

$K$: Strike Price

$T$: Time to Expiration

$r$: Risk-Free Rate

$e$: The base of the natural logarithm (Euler's number)

$N(x)$: The Cumulative Distribution Function (CDF) of the standard normal distribution (calculated using scipy.stats.norm.cdf in the code).

$d_1$ and $d_2$ are intermediate variables calculated as:

$$d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$$

$$d_2 = d_1 - \sigma\sqrt{T}$$