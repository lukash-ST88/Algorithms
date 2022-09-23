nums = [1, 4, 5, 6, 9, 7, 8, 3, 2]
for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
print(nums)
