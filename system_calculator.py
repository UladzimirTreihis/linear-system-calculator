# Print the system in an ordered way
def print_system(dict, unknowns):
    output = ''
    for i in range(unknowns):
        line = ''
        for j in range(unknowns+1):
            if j != unknowns:
                line = line + str(dict[i][j]) + ' '
            else: 
                line = line + '= ' + str(dict[i][j])
        
        output = output + line + '\n'
    print(output + '\n')

# Switch rows with any of the following until the leading coefficient is not 0.
def switch_rows(coefficient_dict, reference_row):
    zero = True
    for i in range(reference_row+1, unknowns):
        if zero == True:
            if coefficients_dict[i][reference_row] != 0:

                temporary = coefficients_dict[i-1]
                coefficients_dict[i-1] = coefficients_dict[i]
                coefficients_dict[i] = temporary
                zero = False
        else:
            continue


unknowns = int(input("please enter a number of unknowns "))
coefficients_dict = {}
print("please, enter the corresponding coefficients including 0 if so ")
for i in range(unknowns):
    c = chr(97 + i)
    coefficients_dict_2 = {}
    for j in range(unknowns+1):
        coefficient = float(input("{}{} = ".format(c, j)))
        coefficients_dict_2[j] = coefficient
    coefficients_dict[i] = coefficients_dict_2

print("Your system is:\n")
print_system(coefficients_dict, unknowns)


# Elimination until upper triangular
for action_row in range(1, unknowns):
    reference_row = action_row - 1
    if coefficients_dict[reference_row][reference_row] == 0:
        switch_rows(coefficients_dict, reference_row)

    for i in range(action_row, unknowns):
        
        elimination_coefficient = -1 * coefficients_dict[i][reference_row] / coefficients_dict[reference_row][reference_row]

        for j in range(unknowns+1):
            coefficients_dict[i][j] = coefficients_dict[i][j] + elimination_coefficient * coefficients_dict[reference_row][j]


# Check whether the system has defined solutions:
solutions = True
for row in range(unknowns):

    if coefficients_dict[row][row] == 0:
        solutions = False

        if coefficients_dict[row][unknowns] == 0:
            print('The system has infinitely many solutions.')
        else: 
            print('The system has no solutions.')

if solutions == True:
    
    # Update the system using back substitution
    last_index = unknowns - 1
    for i in range(unknowns):
        for j in range(unknowns-i, unknowns-i+1):
            coefficients_dict[last_index-i] = coefficients_dict[last_index-i][unknowns] / coefficients_dict[last_index-i][j-1]
            update_index = last_index - i
            try:
                while update_index > 0:

                    
                    coefficients_dict[update_index-1][unknowns] = coefficients_dict[update_index-1][unknowns] - (coefficients_dict[last_index-i] * coefficients_dict[update_index-1][j-1])
                    coefficients_dict[update_index-1][j-1] = 0
                    update_index = update_index - 1
            except:
                continue

    print("\n")
    print("The solutions are the following: \n")
    for i in range(unknowns):
        print("x{}".format(i) + " = " + str(coefficients_dict[i]))




