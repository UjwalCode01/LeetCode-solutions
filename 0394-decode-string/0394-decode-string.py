class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curr_string = ""
        curr_num = 0

        for char in s:
            if char.isdigit():
                # Form multi-digit numbers (e.g., "10[a]")
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                # Push the string built so far and the multiplier onto stack
                stack.append(curr_string)
                stack.append(curr_num)
                # Reset for the inside of the brackets
                curr_string = ""
                curr_num = 0
            elif char == ']':
                # Pop the multiplier and previous string
                num = stack.pop()
                prev_string = stack.pop()
                # Repeat current string and append to previous context
                curr_string = prev_string + num * curr_string
            else:
                # Regular character, append to current string
                curr_string += char

        return curr_string