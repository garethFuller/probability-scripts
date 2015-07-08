
# Value a ball can be (1-49)
possibleValues = range(49)
amountOfBalls = 6

# calculate the number of leafs in the tree for this
# we know we have 49 numbers so when we select one
# number the possible choices for the next number goes down
# by one (no mater what happened in the presvious choice!)

# for our example it would be something like
# 49 * 48 * 47 * 46 * 45 * 44 = 10068347520 (leafs in this example)

# calculate the amount of permitations (sequence of numbers) we could have for
# this combination (this is known as n!) meaning n factorial

# these are the slots for the permitations
# [][][][][][] ..... [] (goes on until we get to one)
# after picking a number to go into the first slot it will look like this
# [49][][][][][] ... []
# 49 being the amount of choices for the slot, after we then move onto
# the next slot we will have 48 choices so
# [49][48][][][][] and so on and so on

# in the case the numbers in the slot are n and n factorial is the
# number of permitations (slots) until we get to 1 this in maths
# is basically like saying
# (49) * (48) * (47) ... (1)

# These comments are also primarily for me btw

# Now if we have n elements 1,2,3 ... n and we want to cerate a
# subset. we need to look at each and decide, going in or not
# e.g. 1 -> yeah, 2 -> no, 3 -> no, 4 -> sure
#
# the next question is how many sub sets are there
# for all elements we have 2 choices, in or out so the value is
# 2 to the power of n
numberOfSubsets = pow(len(possibleValues), 2);

# start odds at 1 (100%)
odds = 1

# quick test to see the probabilty of getting the right set
for i in range(amountOfBalls):
    # probability of next value
    p = float(1) / (len(possibleValues) - i)
    # this below would be with independance
    # p = float(1) / len(possibleValues)
    odds *= float(p)

print "your odds of winning the lottery are:"
print odds

# assuming all balls have an equal probabilty the probabilty of each result is
# 1 / amountOfBalls to the power of possibleValues
probabiltyOfSequence = pow(1 / float(len(possibleValues)), amountOfBalls)
# for example as the probabilty of one is ass likely as another (for now)
# the probabilty of a sequence is as folows
# p(2) * p(3) * p(40) * p(39) * p(20) * p(33) = 1/49 * 1/49 .... (can only multiply assuming independance)
# in this case the probability of any number is 1/49 = 0.02040816326530612
# this value to the power of the amount of balls is pow(1/49, 6) = 7.2247615809006274E-11

print "####################"

print 'The probabilty of any given sequence of there where independance, which there is not, is '
print probabiltyOfSequence