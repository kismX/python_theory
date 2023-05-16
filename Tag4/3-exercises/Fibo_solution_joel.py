# each new number is the sum of the previous two umbers
prevprev = 0
prev = 1
current = 1

# loop for 50 times
for i in range(50): # i for index(iteration/integer), could be another; man nimmt es aber usually
    print(prev)
    prevprev = prev 
    prev = current
    current = prev + prevprev 