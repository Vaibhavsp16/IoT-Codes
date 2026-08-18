import Pyro4

uri = input("Enter the Server URI: ")

calculator = Pyro4.Proxy(uri)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", calculator.add(a, b))
print("Multiplication =", calculator.multiply(a, b))