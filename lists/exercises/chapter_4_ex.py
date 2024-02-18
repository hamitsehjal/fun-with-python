# Working with Lists

magicians=["alice","duro","cacho"]
for magician in magicians:
  print(f"Hi, loved your trick: {magician}")

print(f"Thanks {magician}")

for num in range(10):
  print(num,end="")
print("")
for num in range(5,10):
  print(num,end="")

print("")
# using a Step 
for num in range(5,10,2):
  print(num,end="")

print("")

# Simple statistics in python - min,max,sum methods
nums=[1,2,3,4,5]
print(f"Max: {max(nums)}")
print(f"Min: {min(nums)}")
print(f"Sum: {sum(nums)}")


# List comprehensions
square=[]
for num in range(2,11):
  square.append(num**2)

print(square)

square2=[num**2 for num in range(2,11)]
print(square2)

# Slicing a list
numbers=[num for num in range(10)]
print(numbers)
print(numbers[1:8:2])
print(numbers)
print("Printing the last three elements")
print(numbers[-3:])
