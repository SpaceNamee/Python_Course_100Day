# 0 Default parameter
def num_sum(n, a=3, c=4):
    print(a+c+n)

num_sum(2,3,5)
# 1. *args Unlimited positional Arguments ---------------------------------------------------------
def add(*args):
    print(sum(args))

add(2,2,2,2,2,2)

# 2 **kwargs: Many key arguments
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=5, multiply=4)
