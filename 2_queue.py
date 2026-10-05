class Queue:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.queue = [0] * 100

    def enqueue(self, x):
        if self.rear == 99:
            print("Queue Overflow")
            return

        if self.front == -1:
            self.front = 0

        self.rear += 1
        self.queue[self.rear] = x

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")
            return

        x = self.queue[self.front]
        self.front += 1
        print("Processed Ticket:", x)

    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is Empty")
            return

        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")


q = Queue()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter no: "))

    if ch == 1:
        ticket = int(input("Enter ticket number: "))
        q.enqueue(ticket)

    elif ch == 2:
        q.dequeue()

    elif ch == 3:
        q.display()

    elif ch == 4:
        break

    else:
        print("Invalid choice")