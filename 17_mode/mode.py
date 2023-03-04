def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    counts = {}
    max_val = 1
    max = nums[0]
    for num in nums:
        if num not in set(counts.keys()):
            counts[num] = 1
        else:
            counts[num] += 1
        
        if counts[num] > max_val:
            max_val = counts[num]
            max = num
    
    return max
