# Alec Rizzo
# Python - Homework 2
# In this assign you'll write a program that allows a user to explore/search the periodic
# table of elements and compute the molecular mass of compounds.

def build_periodic_table(filename="periodic_table.txt"):
    input_file = open(filename, 'r')
    table = dict()
    for element in input_file:
        tokens = element.split()
        table[tokens[2]] = (tokens[1], int(tokens[0]), float(tokens[3]))
    return table

def menu(table):
    userVal = 0
    while True:
        try:
            print( "1) Search by symbol/name \n2) Search by atomic mass \n3) Molecular Mass Calculation \n4) Quit")
            userVal = int(input("Please enter number 1 - 4: "))
            if userVal <= 0 or userVal > 4:
                print("Please enter only positive integers, 1 - 4!")
                continue
            break
        except:
            print("Please enter only positive integers, 1 - 4!")

    if userVal == 1:
        userString = input("Please enter a string to search: ")
        userString = userString.lower()
        print_values(search_element_name(table, userString))
        return
    elif userVal == 2:
        print_values(search_element_mass(table))
        return
    elif userVal == 3:
        print("The molecular mass is", calculate_molecular_mass(table))
        return
    elif userVal == 4:
        return "EXIT"
    else:
        print("Something went wrong my friend")

def clean(spaces, length):
    spaces -= length
    spaces = " " * int(spaces)
    return spaces

def search_element_name(table, userString):
    result = dict()
    for key in table:
        temp = key.lower()
        tableValues = table[key]
        elementValues = tableValues[0]
        elementValues = elementValues.lower()

        if userString in temp:
            result[key] = table[key]
        if userString in elementValues:
            result[key] = table[key]
    return result

def search_element_mass(table):
    while True:
        try:
            min = float(input("Please enter a minimum mass: "))
            if min <= 0:
                print("Please enter only positive numbers")
                continue
            break
        except:
            print("Please enter only positive numbers")

    while True:
        try:
            max = float(input("Please enter a maximum mass: "))
            if max <= 0:
                print("Please enter only positive numbers")
                continue
            break
        except:
            print("Please enter only positive numbers")

    result = dict()
    for key in table:
        elementValues = table[key]
        mass = elementValues[2]
        if mass >= min and mass <= max:
            result[key] = table[key]
    return result

def calculate_molecular_mass(table):
    userString = ""
    sum = 0
    while '.' not in userString:
        userString = input("Enter atomic symbol of element ('.' starts calculation): ")
        if userString not in table and userString != '.':
            print("Please enter the element symbol as it is meant to appear")
            userString = ""
            continue
        for key in table:
            if '.' in userString:
                return sum
            if userString == key:
                while True:
                    try:
                        count = int(input("Enter number of atoms of " + userString + " in molecule: "))
                        if count <= 0:
                            print("Please enter only positive numbers")
                            continue
                        break
                    except:
                        print("Please enter only positive numbers")
                valuesOfDict = table[key]
                if userString == key:
                    mass = float(valuesOfDict[2] * count)
                    sum += mass

def print_values(dictValues):
    print(3*" " + "#" + 2*" " + "Name" + 18*" " + "Sym" + 2*" " + "Mass")
    print(50 * "=")
    for symbol in sorted(dictValues.keys()):
        elementValues = dictValues[symbol]
        name = str(elementValues[0])
        number = str(elementValues[1])
        mass = str(elementValues[2])
        print(clean(4, len(number)) + number  + "  " + name + clean(20, len(name)) + clean(5, len(symbol)) + symbol + "  " + mass)
    print(50 * "=")

table = build_periodic_table()

endCondition = ""
while endCondition != "EXIT":
    endCondition = menu(table)
