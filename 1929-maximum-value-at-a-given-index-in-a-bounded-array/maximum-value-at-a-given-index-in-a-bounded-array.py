class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        len_left = index
        len_right = n - index - 1

        val_index = maxSum
        
        def total_sum(val_index):
            return val_index + sum_side(val_index, len_left) + sum_side(val_index, len_right)

        cur_sum = total_sum(val_index)
        res = 0

        # Decrement val_index while the sum exceeds maxSum
        hi = maxSum
        lo = 1
        while ( lo <= hi):
            val_index = (hi-lo)//2 + lo
            cur_sum = total_sum(val_index)
            if (cur_sum > maxSum):
                hi = val_index-1
            else:
                res = val_index
                lo = val_index+1

        return res

def total_subtract(n):
    return n*(n+1)//2

def sum_side(val_index, length):
    m = val_index - 1

    if m >= length:
        hi = total_subtract(m)
        lo = total_subtract(m-length)
        return hi-lo
    elif (m < length):
        hi = total_subtract(m)
        ones = length - m
        return hi + ones