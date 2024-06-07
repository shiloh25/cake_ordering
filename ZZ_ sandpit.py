# initializing string
test_str = 'Valley Road'

print("The original string is : " + str(test_str))

# using any() to check for any occurrence
res = any(chr.isdigit() for chr in test_str)

print("Does string contain any digit ? : " + str(res))