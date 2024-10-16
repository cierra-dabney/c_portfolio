"""
Author: Cierra Dabney
Date: 10/16/2024
Description: This program presents a text based slot machine for the users enjoyment.
             It allows the user to deposit money, bet on lines, spin the slot machine, 
             and tell them their winnings. Shows understanding of basic python concepts
             such as loops, functions, and dictionaries.

"""

import random

#global constants
MAX_LINES =  3
MAX_BET = 100
MIN_BET = 5

#slot machine build
ROWS = 3
COLS = 3

#amount of each symbol
symbolCount = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

#value of each symbol
symbolValue = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def checkWinnings(columns, lines, bet, values):
    winnings = 0
    winningLines = []
    for line in range(lines):#looping through every row that is being checked
        symbol = columns[0][line]#check symbol in the first column of the current row
        for column in columns:#loop through the columns looking for the symbol
            symbolToCheck = column[line]
            if symbol != symbolToCheck:#breaks if they are not the same (didnt win)
                break
        else:
            winnings += values[symbol] * bet#won if symbols are the same, value of the symbol times tbeir bet
            winningLines.append(line + 1)#gives the line user won on

    return winnings, winningLines

#randomly picks number of rows inside each column and the symbols inside
def getSlotMachineSpin(rows, cols, symbols):
    allSymbols = []
    for symbol, symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)
    
    columns = []#defines the columns list
    #for loop creates a column for every column in program
    for _ in range(cols):
        column = []#defines the column list
        currentSymbols = allSymbols[:]#creates copy of current symbols instead of a reference
        for _ in range(rows):
            value = random.choice(currentSymbols)#picks rrandom vlaue form list
            currentSymbols.remove(value)#the rand value cannot be chosen again
            column.append(value)#adds removed valued to colunm

        columns.append(column)#adds column to columns list

    return columns

#transposing
#loops through every row and every column for the row you are on
def printSlots(columns):
    for row in range(len(columns[0])):#looping through every single row
        for i, column in enumerate(columns):#looping through every column; items inside column
            if i != len(columns) - 1:#max index to access an element in columns list
                print(column[row], end= " | ")#end tells the program where to start the next line
            else:
                print(column[row], end="")

        print()#brings user down to the next line


#collecting user input through function deposit
def deposit():
    while True:
        amount = input("Hello, what would you like to deposit? Enter amount : $")
        #tells you if valid whole number
        if amount.isdigit():
            amount = int(amount)#converts to integer
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0...")

    return amount

def getNumberOfLines():
    while True:
        line = input("How many lines would you like to bet on? Enter amount (1 -" + str(MAX_LINES)+ ")? ")
        #tells you if valid whole number
        if line.isdigit():
            line = int(line)#converts to integer
            if 1 <= line <= MAX_LINES:
                break #break if not inbetween 1 and MAX_LINES
            else:
                print("Enter valid number of lines (1 - " + str(MAX_LINES) + ")")

    return line

def getBet():
    while True:
        amount = input("What would you like to bet on each line? Enter amount : $")
        #tells you if valid whole number
        if amount.isdigit():
            amount = int(amount)#converts to integer
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Your betting amount must be between ${MIN_BET} - ${MAX_BET}.")#f-string for data type conversion
        else:
            print("Please enter a number.")

    return amount

def spin(balance):
    lines = getNumberOfLines()
    while True:
        bet = getBet()
        totalBet = bet * lines

        if totalBet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is: ${balance}")
        else:
            break


    print (f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${totalBet}")

    slots = getSlotMachineSpin(ROWS, COLS, symbolCount)
    printSlots(slots)
    winnings, winningLines = checkWinnings(slots, lines, bet, symbolValue)
    print(f"You won ${winnings}!!!")
    print(f"You won on lines: ", *winningLines)#splat operator

    return winnings - totalBet


#main function
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play(q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}!")

main()
