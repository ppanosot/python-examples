# the if...else in the most basic form
# the else block runs when all the conditions
# preceeding it are not true
# the else block is not necessary (i.e. you can have an if...else statement
# without the else part).
a = 10
b = 9
if a == b:
    print('a and b are equal')
else:
    print('a and b are not equal')
    
print('-'*30) # in python, strings can be added and multiplied

# for a single if...else statement, only the block under the FIRST true
# condition will be run
if a< b:
    print('a is less than b') # this wont run
if a >= b:
    print('a is greater or equal to b') #this will run
elif a == 10:
    print('a = 10') # this wont run even though it's true
elif b == 9:
    print('b = 9') # this also wont

print('-'*30)

# this is two if...else statements (without the elses)
# and they are both true, so they both run
b = 10
if a >= b:
    print('a is greater or equal to b')
if a <= b:
    print('a is less or equal to b')
    
print('-'*30)


# if...else statements can be nested arbitrarily
a = 11
c = 8
# outter if..else statement
if a > b:
    print('a is greater than b')
    # inner if...else statement
    if a > c:
        print('a is greater than both b and c')
    else:
        print('a is greater than b but not greater than c')
# else block of the outer if...else statement
else:
    print('a is not greater than b')
