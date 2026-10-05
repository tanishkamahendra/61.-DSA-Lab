class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insert_end(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = newNode

    def delete_beginning(self):
        if self.head is None:
            print("List is Empty")
            return

        print("Deleted Book:", self.head.data)
        self.head = self.head.next

    def display(self):
        if self.head is None:
            print("List is Empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data)
            temp = temp.next


l = LinkedList()

while True:
    print("\n1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter no: "))

    if ch == 1:
        book = input("Enter book name: ")
        l.insert_beginning(book)

    elif ch == 2:
        book = input("Enter book name: ")
        l.insert_end(book)

    elif ch == 3:
        l.delete_beginning()

    elif ch == 4:
        l.display()

    elif ch == 5:
        break

    else:
        print("Invalid choice")