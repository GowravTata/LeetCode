def removeElement(nums, val):
    nums = [num for num in nums if num != val]
    return nums


nums = [0, 1, 2, 2, 3, 0, 4, 2]
value = 2
# print(removeElement(nums, value))

all_nums = list(filter(lambda x: x != 2, nums))
print(all_nums)
