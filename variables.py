# in python a variable is basically a name that is assigned a value.
# the value could be anything. e.g. another variable, a function, a module, etc.

a = 'blah blah'
b = 'duh'

# when you assign a value to a name, the name is binded to that value
# when the name is referred to, it returns the value of the object to which it is binded
b = a # the name 'b' is binded to the variable 'a'
print(b) # will print 'blah blah'

# some types of object (pretty much everything is an object in python) can be changed
# for example, a list, which we did today
list1 = [1, 2 ,3 ,4]
list1[1] = 3 # the 2nd item in the list
print (list1) # will print [1, 3, 3, 4]

list2 = list1 # now both variables are binded to the same list

list2[0] = 5 # since list1 and list2 are binded to the same list object
             # list1 gets changed too
print(list1) # will print [5, 3, 3,4]

# this is not true for literals (the easiest way to think of literals is
# the value that you literally typed out. strings, numbers)

a = 10
b = a
print(b) # will print 10

b = 5 # we are assigning a new literal 5 to the variable b,
      # not changing the literal 10 to 5, because literals cant be changed
      #(how can you change a value 10 to 5, right?)
print(b) # will print the new value 5
print(a) # a is still 10, not 5

# back to name binding. you can even do this
print = 10  # now you just lost access to the built in print function
            # print becomes a variable with value 10
            # if you run this script and type print then enter(return) you get a 10
            # if you try print('hello') you get an error
            
