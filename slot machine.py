#slot machine
import random
#get 3 in a row you win

rows = 3
cols = 3

#symbols for slot
symbol_count={
    "@": 2,
    "&": 5,
    "#": 4,
    "*": 8
}

symbol_value ={
    "@": 3,
    "&": 4,
    "#": 2,
    "*": 3
}

Maximum_betting_lines = 3
Maximum_betting_amount = 100
Minimum_beetting_amount = 1

def check_winning(columns, lines, bet, values):
    winning = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            check_symbol = column[line]
            if symbol != check_symbol:
                break
        else: 
            winning += values[symbol]*bet
            winning_lines.append(line*1)

    return winning, winning_lines

def get_spin(rows, cols, symbols):
    all_symbols = [4]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns =[]
    for _ in range(rows):
        column =[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end= " | ")
            else:
                print(column[row], end= "")

        print()


#get user input
def deposit():
    while True:
        amount = input("How much do you want to deposit?: ")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a valid number.")

    return amount

def number_of_lines():
    while True:
        lines = input("Enter number of lines you want to bet on (1-"+ str(Maximum_betting_lines)+ ") ")
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <= Maximum_betting_lines:
                break
            else:
                print("Enter valid number of lines.")
    return lines

def get_betting():
    while True:
        amount = input("How much would you like to bet? " + "("+str(Minimum_beetting_amount)+"-"+str(Maximum_betting_amount)+") ")
        if amount.isdigit():
            amount = int(amount)
            if amount >= Minimum_beetting_amount and amount <= Maximum_betting_amount:
                break
            else:
                print("Enter a valid amount.")
        else:
            print("Please enter a digit.")

    return amount

def game(balance):
    lines = number_of_lines()

    while True:
        bet = get_betting()
        total_bettings = bet*lines

        if total_bettings > balance:
            print(f"Insufficient amount, your balance is R{balance}")
        else:
            break

    print(f"you are betting R{bet} on {lines} lines. Your total bet is equal to:{total_bettings} ")
    print(balance, lines)

    slot = get_spin(rows, cols, symbol_count)
    print_slot_machine(slot)
    winnings, winning_lines = check_winning(slot, lines, bet, symbol_value)
    print(f"You won R{winnings}")
    print(f"You won on:", *winning_lines)
    return winnings - total_bettings

def main():
    balance= deposit()
    while True:
        print(f"Your current balance is R{balance}")
        play = input("Press enter to play or Q to quit")
        if play == "q" or play == "Q":
            break
        balance += game(balance)

    print(f"Yor balance is R{balance}")

main()

