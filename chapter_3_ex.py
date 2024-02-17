
# Lists in Python

names=["hamit",5,"youo"]

print(names)
print(type(names[1]))

print(f"Without Formatting: {names[0]}")

print(f"With Formatting: {names[0].title()}")

## Adding to a list
names.append("mango")

print(f"Using append() method: {names}")

## using insert(index,value)

names.insert(2,10)
print(names)

names.insert(10,100)
print(names)

## Deleting from a list

del names[1]

print(names)

popped_value=names.pop()

print(names)
print(popped_value)

# using pop to delete from any index
poppy=names.pop(2)
print(names)
print(poppy)

names.insert(1,"ducati")
print(names)
names.remove('ducati')
print(names)

## Organizing a List

### RE-arrange the elements (sorting)

### in-place sorting
cars=["bmw","audi","toyota","suburu"]

print(f"Without Sorting: {cars}")
cars.sort(reverse=True)
print(f"With Sorting:{cars}")

### reversing a list
cars.reverse()
print(cars)
