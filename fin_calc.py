def present_value(future_value, discount_rate, periods):
    """
    Calculate the present value of a future amount of money.

    Parameters:
    - future_value (float): The amount of money in the future.
    - discount_rate (float): The annual discount rate (as a decimal, e.g., 0.05 for 5%).
    - periods (int): The number of periods (usually years) until the future value is received.

    Returns:
    - float: The present value.
    """
    return future_value / ((1 + discount_rate) ** periods)

def future_value(present_value, interest_rate, periods):
    """
    Calculate the future value of money.

    Parameters:
    present_value (float): The initial amount of money.
    interest_rate (float): The interest rate per period (as a decimal, e.g., 0.05 for 5%).
    periods (int): The number of periods (e.g., years).

    Returns:
    float: The future value of the investment.
    """
    fv = present_value * (1 + interest_rate) ** periods
    return round(fv, 2)

# Example usage:
pv = 1000       # $1,000 initial investment
rate = 0.05     # 5% annual interest
years = 10      # 10 years

fv = future_value(pv, rate, years)
print(f"Future Value: ${fv:,.2f}")

# Example usage:
fv = 1000000       # Future value in dollars
rate = 0.05     # 5% annual discount rate
years = 20        # Number of years

pv = present_value(fv, rate, years)
print(f"Present Value: ${pv:,.2f}")