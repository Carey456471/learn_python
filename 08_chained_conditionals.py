x = 7
y = 8
z = 0

result1 = x == y
result2 = y > x
result3 = z < x + 2

# or => same as ||
# and => same as &&
# not => same as !
result4 = result1 or result2 or result3 
print(result4)

print(not(False and True))