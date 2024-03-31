def test_values(func):
    def wrapper():
        import random
        values = random.randint(1,70) 
        balues = random.randint(1,68)
        print(f"values are: ", {values,balues})
        func(values,balues)
    return wrapper()

@test_values
def sum(x,y):
    result = x + y
    print(result)