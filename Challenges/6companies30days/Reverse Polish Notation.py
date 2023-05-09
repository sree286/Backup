class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        for token in tokens:
            if any(map(str.isdigit,token)):
                self.stack.append(token)
            else:
                b = int(self.stack.pop())
                a = int(self.stack.pop())
                if token == "+":
                    c = a+b
                elif token == "-":
                    c = a-b
                elif token == "/":
                    c = a/b
                elif token == "*":
                    c = a*b
                else:
                    print(token)
                self.stack.append(c)
        return int(self.stack[0])