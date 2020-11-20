class Solution:
    def decodeString(self, s: str) -> str:
        cur_str, cur_num, stack = '', 0, []
        for c in s:
            if c == '[':
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str = ''
                cur_num = 0
            elif c == ']':
                num = stack.pop()
                pre_str = stack.pop()
                cur_str = pre_str + num * cur_str
            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)
            else:
                cur_str += c
        return cur_str