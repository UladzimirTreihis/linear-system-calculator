# linear-system-calculator
This short code in python calculates the unknowns of a system of linear equations. It first simplifies the system into the upper-triangular form. Then it uses back substitution. 


Usage example.


Given a system like the following:

2x + y - 2z = -4

3x + 3z = 10.5

x - y + 4z = 13

Enter the number of unknows: 3

Note the way of the coefficient submission:

a0 = 2

a1 = 1

a2 = -2

a3 = -4

b0 = 3

b1 = 0

b2 = ...

...

The output is in the following format:

'''

The solutions are the following: 

x0 = 2.0

x1 = -5.0

x2 = 1.5

'''
