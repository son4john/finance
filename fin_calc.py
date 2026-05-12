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
    return round(future_value / ((1 + discount_rate) ** periods), 2)

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

def pmt(principal, annual_rate, years):
    """
    Calculate the fixed periodic (monthly) payment for a loan.

    Parameters:
    - principal (float): The loan amount.
    - annual_rate (float): The annual interest rate (as a decimal, e.g., 0.05 for 5%).
    - years (int): The loan term in years.

    Returns:
    - float: The fixed monthly payment.
    """
    r = annual_rate / 12
    n = years * 12
    payment = principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return round(payment, 2)


def amortization_schedule(principal, annual_rate, years):
    """
    Generate a full amortization schedule for a loan.

    Parameters:
    - principal (float): The loan amount.
    - annual_rate (float): The annual interest rate (as a decimal, e.g., 0.05 for 5%).
    - years (int): The loan term in years.

    Returns:
    - list of dicts: Each entry contains payment number, payment amount,
                     principal paid, interest paid, and remaining balance.
    """
    monthly_payment = pmt(principal, annual_rate, years)
    r = annual_rate / 12
    balance = principal
    schedule = []

    for month in range(1, years * 12 + 1):
        interest = round(balance * r, 2)
        principal_paid = round(monthly_payment - interest, 2)
        balance = round(balance - principal_paid, 2)
        schedule.append({
            "month": month,
            "payment": monthly_payment,
            "principal": principal_paid,
            "interest": interest,
            "balance": max(balance, 0)
        })

    return schedule


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