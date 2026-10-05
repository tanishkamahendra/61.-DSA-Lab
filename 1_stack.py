class Stack:
    def __init__(self):
        self.TOP = -1
        self.st = [0] * 100

    def push(self, x):
        if self.TOP == 99:
            print("Stack Overflow")
            return

        self.TOP += 1
        self.st[self.TOP] = x

    def pop(self):
        if self.TOP == -1:
            print("Stack Underflow")
            return

        x = self.st[self.TOP]
        self.TOP -= 1
        print("Processed Book:", x)

    def display(self):
        if self.TOP == -1:
            print("Stack is Empty")
            return

        for i in range(self.TOP, -1, -1):
            print(self.st[i])


s = Stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter no: "))

    if ch == 1:
        book = input("Enter book name: ")
        s.push(book)

    elif ch == 2:
        s.pop()

    elif ch == 3:
        s.display()

    elif ch == 4:
        break

    else:
        print("Invalid choice")