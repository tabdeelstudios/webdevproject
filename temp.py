def dominantIndex(nums):
    max_index = -1
    max_num = -1
    second_max_num = -1
    
    for i, num in enumerate(nums):
        if num > max_num:
            second_max_num = max_num
            max_num = num
            max_index = i
        elif num > second_max_num:
            second_max_num = num
    
    if max_num >= 2 * second_max_num:
        return max_index
    else:
        return -1

# Example usage:
nums = [3, 6, 1, 0]
print(dominantIndex(nums))  # Output: 1
