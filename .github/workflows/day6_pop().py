values = [5,10,15]
values.pop()
print(values)
values = [5,15,25]
x = values.pop()
print(x)
print(values)
data = [100,200,300]
data.pop(0)
print(data)
nums =[1,2,3,4,5]
nums.pop()
nums.append(10)
print(nums)

a = [50]
a.pop()
print(a)
#remove all elements using pop
nums = [1,2,3]

while nums:
    nums.pop()
    
print(nums)
#count how many times pop()Runs
nums = [10,20,30,40]
count = 0

while nums:
    nums.pop()
    count += 1

print("pop count =",count)
#Remove Even Numbers Using pop
nums = [1,2,3,4,5,6]
i = 0
while i < len(nums):
    if nums[i] % 2 == 0:
        nums.pop(i)
        
    else:
        i += 1
print(nums)