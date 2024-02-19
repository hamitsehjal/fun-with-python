# loop that counts 1-10 but only prints odd number in the range
for num in range(1,11):
    if num%2 == 0:
        # num is even
        continue
    print(num)
