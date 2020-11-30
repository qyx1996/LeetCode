class SStack:
    def __init__(self):
        self._elems = [] # 使用list存储栈元素

    def is_empty(self):
        return self._elems == []

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop()

    def top(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.top()")
        return self._elems[-1]

class Solution:
    def isValid(self, s: str) -> bool:
        stack = SStack()
        left_parens = "([{"
        right_parens = ")]}"
        parens = {")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in left_parens:
                stack.push(i)
            elif i in right_parens:
                if stack.is_empty():
                    return False
                if parens[i] != stack.pop():
                    return False
        if stack.is_empty():
            return True
        return False