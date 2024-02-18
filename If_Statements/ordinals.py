# Create ordinals numbers

nums=[num for num in range(1,6)]
ordinals=[]
for num in nums:
    if num==1:
        ordinals.append("First")
    elif num==2:
        ordinals.append("Second")
    elif num==3:
        ordinals.append("Third")
    elif num==4:
        ordinals.append("Fourth")
    elif num==5:
        ordinals.append("Fifth")

for num,ordinal in zip(nums,ordinals):
    print(num,ordinal)
