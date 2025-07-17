class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        for bracket in s:
            if bracket in bracket_map.values():
                stack.append(bracket)
            elif bracket in bracket_map:
                if stack and stack[-1] == bracket_map[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return not stack