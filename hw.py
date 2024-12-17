x = input("Enter the value of x:")
y = input("Enter the value of y:")
z = input("Enter the value of z:")

temp = x
x = y
y = temp 
z = x 
x = temp
y = z

print("\n AFter Swapping")
print(x)
print(y)
print(z)