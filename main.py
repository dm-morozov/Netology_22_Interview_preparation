

# Задача 1
class Stack:

    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return not self.items
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)

        
        
stack = Stack()
print(stack.is_empty())
print(stack.size())
print(stack.pop())
stack.push(2)
stack.push(3)
stack.push(4)
print(stack)
print(stack.pop())
print(stack)
print(stack.peek())
print(stack)
print(stack.size())


print(stack.pop())
print(stack.pop())


# Задача 2
# Используя стек из задания 1, решите задачу на проверку сбалансированности скобок. 
# Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий ему закрывающий, 
# и пары скобок правильно вложены друг в друга.

def is_balanced(brackets):
    stack = Stack()
    for item in brackets:
        if item in '{[(':
            stack.push(item)
        else:
            if stack.is_empty():
                return False
            if item == ']' and stack.peek() != '[':
                return False
            if item == '}' and stack.peek() != '{':
                return False
            if item == ')' and stack.peek() != '(':
                return False
            stack.pop()

    return stack.is_empty()


brackets = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}', 
    '{{[()]}}',
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]

print(['Сбалансированно' if is_balanced(bracket) else 'Несбалансированно' for bracket in brackets])
