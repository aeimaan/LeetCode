class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # get the len of the strings individually
        if len(num1) == 0: return num2
        elif len(num2) == 0: return num1

        num1 = num1[::-1]
        num2 = num2[::-1]

        max_len = max( len(num1) , len(num2))
        res = ""
        carry = 0

        for i in range(max_len):
            cur = ""
            if i > len(num1)-1:
                cur = int(num2[i]) + carry
                carry = 0
            elif i > len(num2)-1:
                cur = int(num1[i]) + carry
                carry = 0
            else:
                cur = int(num1[i]) + int(num2[i]) + carry
            carry = cur // 10
            cur = cur % 10
            res += str(cur)
        if carry == 1:
            res += str(1)
        return res[::-1]

