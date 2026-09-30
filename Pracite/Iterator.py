nums = [1,2,3,4,5,6]

for i in nums :
    print(i , end=",")

iterator = iter(nums)

print("\n",type(iterator))
print(iterator)
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(next(iterator))