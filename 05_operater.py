x = 9
y = 3
#result = x + y
#result = x - y
#result = x * y
result = x / y          # return float
result = int(x / y)     # return int
result = x ** y         # pow(9, 3)

x = 10
result = x // y         # ignore decimal point

result = x % y          # same as java/c++

print(result)

num = input("Number: ") # string
#print(num - 5)  #runtime error
print(int(num) - 5)
print(float(num) - 5)