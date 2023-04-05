def sum_it(x, y):
    return x + y

def sub_it(x, y):
    return x - y

def prod(x, y):
    return x * y

def div_it(x, y):
    # return x / y
    if y == 0:
        try:
            return x / 0
        except:
            return "Can't divide by zero! Try again)"

def pow_it(x, y):
    return x ** y