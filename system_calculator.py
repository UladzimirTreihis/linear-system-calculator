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

if coefficients_dict[0][0] == 0:
    zero = True
    for i in range(unknowns):
        if zero == True:
            if coefficients_dict[i][0] != 0:
                for j in range(unknowns+1):
                    temporary = coefficients_dict[0][j]
                    coefficients_dict[0][j] = coefficients_dict[i][j]
                    coefficients_dict[i][j] = temporary
                zero = False
        else:
            continue

# Elimination until upper triangular
for starting_line in range(1, unknowns):

    for i in range(starting_line, unknowns):

        non_zero_coefficient_position = starting_line - 1
        
        elimination_coefficient = -1 * coefficients_dict[i][non_zero_coefficient_position] / coefficients_dict[starting_line-1][non_zero_coefficient_position]

        for j in range(unknowns+1):
            coefficients_dict[i][j] = coefficients_dict[i][j] + elimination_coefficient * coefficients_dict[starting_line-1][j]

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


    

