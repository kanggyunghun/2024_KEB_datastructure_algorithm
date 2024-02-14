def push(data):
    if top >= SIZE-1:
        print("Stack is full")
        return
    top += 1
    return stack[top]

def pop():
    if top == -1:
        print("Stack is empty")
        return
    top -= 1
    data = stack[top]
    stack[top] = None
    return data

def peek():
    if top == -1:
        print("Stack is empty")
        return
    return stack[top]

if __name__ == "__main__":
