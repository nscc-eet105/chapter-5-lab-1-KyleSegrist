# Code contains four problems.
STATE_TAX_RATE = .051
COUNTY_TAX_RATE = .025


def main():
    print('This program will calculate your taxes!\n')

    sale = float(input('How much is the cost of your purchase? '))
    state_tax = calculate_state_tax(sale, STATE_TAX_RATE)  #state tax variable was undefined KS
    county_tax = calculate_county_tax(COUNTY_TAX_RATE, sale)
    total_cost = sale + state_tax + county_tax

    print('\nSale amount: $', format(sale, '.2f'), sep='')
    print('State tax  : $', format(state_tax, '.2f'), sep='')
    print('County tax : $', format(county_tax, '.2f'), sep='')
    print('Total cost : $', format(total_cost, '.2f'), sep='')


def calculate_state_tax(sale, STATE_TAX_RATE):  #Incorrect / undefined variables called KS
    return (sale * STATE_TAX_RATE)                  #(sales_amount * tax_rate)


def calculate_county_tax(sale,COUNTY_TAX_RATE):  #Incorrect / undefined variables called KS
    return (sale * COUNTY_TAX_RATE)                 # taxes = amount * rate
    #taxes = amount * rate


main()