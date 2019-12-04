def first_last6(nums):
  if nums[0] == 6:
    return True
  elif nums[2] == 6:
    return True
  else:
    return False
nums = 1,2,6   
print(first_last6(nums))