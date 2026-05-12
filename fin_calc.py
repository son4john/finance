def present_value(future_value, discount_rate, periods):
    """Calculate the present value of a future amount of money.

    Args:
        future_value (float): The amount of money in the future.
        discount_rate (float): The annual discount rate as a decimal (e.g., 0.05 for 5%).
        periods (int): The number of periods until the future value is received.

    Returns:
        float: The present value.
    """
    return round(future_value / ((1 + discount_rate) ** periods), 2)


def future_value(present_value, interest_rate, periods):
    """Calculate the future value of money.

    Args:
        present_value (float): The initial amount of money.
        interest_rate (float): The interest rate per period as a decimal (e.g., 0.05 for 5%).
        periods (int): The number of periods (e.g., years).

    Returns:
        float: The future value of the investment.
    """
    return round(present_value * (1 + interest_rate) ** periods, 2)


def pmt(principal, annual_rate, years):
    """Calculate the fixed monthly payment for a loan.

    Args:
        principal (float): The loan amount.
        annual_rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%).
        years (int): The loan term in years.

    Returns:
        float: The fixed monthly payment.
    """
    r = annual_rate / 12
    n = years * 12
    return round(principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1), 2)


def amortization_schedule(principal, annual_rate, years):
    """Generate a full amortization schedule for a loan.

    Args:
        principal (float): The loan amount.
        annual_rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%).
        years (int): The loan term in years.

    Returns:
        list[dict]: Each entry contains month, payment, principal, interest, and balance.
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
            "balance": max(balance, 0),
        })

    return schedule


def extra_payment_savings(principal, annual_rate, years, extra_payment):
    """Calculate how much sooner a loan is paid off with extra monthly principal payments.

    Args:
        principal (float): The loan amount.
        annual_rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%).
        years (int): The original loan term in years.
        extra_payment (float): Additional principal paid each month on top of the standard payment.

    Returns:
        dict: Contains original_months, new_months, months_saved, years_saved,
              original_interest, new_interest, and interest_saved.
    """
    monthly_payment = pmt(principal, annual_rate, years)
    r = annual_rate / 12

    def simulate(extra):
        balance = principal
        total_interest = 0
        months = 0
        while balance > 0:
            interest = round(balance * r, 2)
            total_interest += interest
            balance -= round(monthly_payment - interest + extra, 2)
            months += 1
        return months, round(total_interest, 2)

    original_months, original_interest = simulate(0)
    new_months, new_interest = simulate(extra_payment)

    return {
        "original_months": original_months,
        "new_months": new_months,
        "months_saved": original_months - new_months,
        "years_saved": round((original_months - new_months) / 12, 1),
        "original_interest": original_interest,
        "new_interest": new_interest,
        "interest_saved": round(original_interest - new_interest, 2),
    }


if __name__ == "__main__":
    # Future Value: $1,000 at 5% over 10 years
    fv = future_value(1000, 0.05, 10)
    print("Future Value: ${:,.2f}".format(fv))

    # Present Value: $1,000,000 in 20 years at 5% discount rate
    pv = present_value(1000000, 0.05, 20)
    print("Present Value: ${:,.2f}".format(pv))

    # PMT: monthly payment on a $300,000 loan at 6% over 30 years
    monthly = pmt(300000, 0.06, 30)
    print("Monthly Payment: ${:,.2f}".format(monthly))

    # Amortization Schedule: first 3 months of a $300,000 loan at 6% over 30 years
    schedule = amortization_schedule(300000, 0.06, 30)
    print("\nAmortization Schedule (first 3 months):")
    print("{:<8} {:<12} {:<12} {:<12} {}".format(
        "Month", "Payment", "Principal", "Interest", "Balance"
    ))
    for row in schedule[:3]:
        print("{:<8} ${:<11,.2f} ${:<11,.2f} ${:<11,.2f} ${:,.2f}".format(
            row["month"], row["payment"], row["principal"],
            row["interest"], row["balance"]
        ))

    # Extra Payment Savings: $200 extra/month on a $300,000 loan at 6% over 30 years
    savings = extra_payment_savings(300000, 0.06, 30, 200)
    print("\nExtra Payment Savings ($200/month):")
    print("Time saved:      {} months ({} years)".format(
        savings["months_saved"], savings["years_saved"]
    ))
    print("Interest saved:  ${:,.2f}".format(savings["interest_saved"]))
