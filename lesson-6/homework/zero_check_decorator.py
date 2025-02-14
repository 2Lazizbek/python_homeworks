def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        else:
            return int(func(a, b)) if func(a, b).is_integer() else func(a, b)
    return wrapper

         

@check
def div(a, b):
   return a / b

print(div(6, 2))
print(div(6, 0))