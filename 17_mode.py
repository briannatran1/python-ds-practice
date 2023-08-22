def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # make freq counter and get max value

    # our solution
    #
    # highest_count = 0
    # highest_val = 0

    # for num in nums:
    #     count = nums.count(num)
    #     if count > highest_count:
    #         highest_count = count
    #         highest_val = num

    # return highest_val
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    max_value = max(counts.values())

    for (num, freq) in counts.items():
        if freq == max_value:
            return num
