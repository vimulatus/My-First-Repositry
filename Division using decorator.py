def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! Cannot divide")
            return
        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

a = int(input())
b = int(input())
divide(a, b)
