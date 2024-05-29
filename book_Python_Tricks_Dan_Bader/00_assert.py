'''
    use assert to raise AssertionError in case of unexpected values
    In case an assertion triggered the program will fail and will return the stacktrace for easy debugging

    Assertion should not be used to capture runtime errors (as replacement of exception)
    Assertion should used to easyly identify bugs in the code


    **** Assertions can be disabled in Python interpriter
         Do not use Assertions for critical checks 
'''

def apply_discount(product, discount):

    assert 0 <= discount < 1, f"Dicount should be 0<=price<1 and {discount} passed"

    return product['price'] * (1.0 - discount)



product = {"name": "pA", "price": 10}

print(apply_discount(product, 1000))