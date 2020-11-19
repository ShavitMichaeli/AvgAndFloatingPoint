x = []  # initialize list of items named as x
y = 0  # initialize variable
floating = 0  # initialize flag variable
n = 0
while n < 10:  # int the first loop, were, entering the numbers one by one
    y = float(input("Please enter number :"))  # setting and casting y as floating point
    x.append(y)  # adding the value of y into list 'x'
    n = n + 1  # loop stop condition
n = 0  # setting n to zero for future use

# loop is set to check if there is a floating point on one the items that has been set in the list x
# the if statement checks if the floating point of variable not equals to the integer of the variable
# if its not, the flag 'floating' change into '1' which means there is a floating point

while n < 10:
    if int(x[n]) != float(x[n]):
        floating = 1
        n = n + 1
        continue
    else:
        x[n] = int(x[n])
        n = n + 1

# if the flag is equals to '1' the function will sum and get
# average as floating point,if not as integer

if floating == 1:
    print("The Average is:", sum(x) / 10.0)
else:
    print("The Average is:", int(sum(x) / 10))
