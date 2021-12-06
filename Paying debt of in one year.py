def main():
    #balance_after_one_year()
    #find_fixed_monthly_payment()
    bisection_search()
"""
def balance_after_one_year():
    balance = 484
    annualInterestRate = 0.2
    monthlyPaymentRate = 0.04
    Monthly_interest_rate = annualInterestRate / 12
    for i in range(12):
        Minimum_monthly_payment = balance * monthlyPaymentRate
        Monthly_Unpaid_balance = balance - Minimum_monthly_payment
        balance = Monthly_Unpaid_balance + (Monthly_interest_rate * Monthly_Unpaid_balance)
    print("Remaining balance:", round(balance, 2))

def find_fixed_monthly_payment():
    balance = 4773
    annualInterestRate = 0.2

    Minimum_monthly_payment = 10
    Monthly_interest_rate = annualInterestRate / 12
    loop_balance = balance
    while True:
        for i in range(12):
            Monthly_Unpaid_balance = loop_balance - Minimum_monthly_payment
            loop_balance = Monthly_Unpaid_balance + (Monthly_interest_rate * Monthly_Unpaid_balance)
        if loop_balance <= 0:
            break
        else :
            loop_balance = balance
            Minimum_monthly_payment += 10

    print("Lowest Payment:", Minimum_monthly_payment)
"""

def bisection_search():
    balance = 423197
    annualInterestRate = 0.21

    Monthly_interest_rate = annualInterestRate / 12.0
    Monthly_payment_lower_bound = balance / 12
    Monthly_payment_upper_bound = (balance * (1 + Monthly_interest_rate)**12) / 12

    Minimum_monthly_payment = (Monthly_payment_lower_bound + Monthly_payment_upper_bound) / 2
    epsilon = 0.01

    remaining_balance = balance
    for i in range(12):
        Monthly_Unpaid_balance = remaining_balance - Minimum_monthly_payment
        remaining_balance = Monthly_Unpaid_balance + (Monthly_interest_rate * Monthly_Unpaid_balance)

    while abs(remaining_balance) >= epsilon :
        if remaining_balance < 0 :
            Monthly_payment_upper_bound = Minimum_monthly_payment
        else :
            Monthly_payment_lower_bound = Minimum_monthly_payment

        Minimum_monthly_payment = (Monthly_payment_lower_bound + Monthly_payment_upper_bound) / 2
        remaining_balance = balance
        for i in range(12):
            Monthly_Unpaid_balance = remaining_balance - Minimum_monthly_payment
            remaining_balance = Monthly_Unpaid_balance + (Monthly_interest_rate * Monthly_Unpaid_balance)


    print("Lowest Payment:", round(Minimum_monthly_payment, 2))


if __name__ == '__main__':
    main()