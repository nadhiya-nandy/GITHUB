#THIS IS A SAMPLE PROGRAM FOR PRINITING EVEN NUMBERS USING GENERATOR

"""
in this function I used yield statement it is used to return value as well keep
track of previous value
"""
def even():
   n=0
   while True:
        yield n
        n = n + 2 
"""
Here the generator function is assigned to a varible of name copy

"""
copy=even()

"""
This for loop is using range it holds value upto the given limit like a list . But it requires only few memory compared to a list

The next statment help help me to get the ext value of the generator function

"""

for i in range(200):
    print(next(copy))

