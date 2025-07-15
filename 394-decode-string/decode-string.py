class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                # Gather backwards
                word = ""
                tmp = stack.pop(-1)
                while tmp != '[':
                    word += tmp
                    tmp = stack.pop(-1)
                # Reverse the word
                word = word[::-1]
                num = ""
                while stack and stack[-1].isnumeric():
                    num += stack.pop(-1)
                num = num[::-1]
                for i in range(int(num)):
                    for c in word: stack.append(c)
        return "".join(stack)