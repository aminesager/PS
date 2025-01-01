# Initial investment, monthly interest rate, and number of months
initial_investment = 500000  # $300,000
monthly_interest_rate = 0.12  # 3% monthly growth
years = 10
months = years * 12

# Compound interest formula: A = P * (1 + r/n)^(nt)
final_amount = initial_investment * (1 + monthly_interest_rate) ** months
print(final_amount)
