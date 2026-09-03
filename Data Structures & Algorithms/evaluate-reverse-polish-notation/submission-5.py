class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        myStack = []

        for element in tokens:
            if element == "+":
                myStack.append(myStack.pop() + myStack.pop())
            elif element == "-":
                a, b = myStack.pop(), myStack.pop()
                myStack.append(b-a)
            elif element == "*":
                myStack.append(myStack.pop() * myStack.pop())
            elif element == "/":
                a, b = myStack.pop(), myStack.pop()
                myStack.append(int(b/a))
            else:
                myStack.append(int(element))
        return myStack[0]

        