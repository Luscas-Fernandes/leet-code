import time

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None


    def addHead(self, value):
        new_node = Node(value)
        
        if self.head == None: 
            self.tail = new_node
        else:
            self.head.previous = new_node 
            new_node.next = self.head 
    
        self.head = new_node


    def addTail(self, value):
        new_node = Node(value)

        if self.tail == None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail

        self.tail = new_node


    def removeHead(self):
        if self.head == None:
            return
        
        if self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None


    def removeTail(self):
        if self.tail == None:
            return

        if self.tail.previous == None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None


    def searchList(self):
        search = self.head

        while search:
            if search.next:
                print(search.value, "-> ", end='', flush=True)
            else:
                print(search.value)

            search = search.next

        return None
        
    def searchItemList(self, value):
        search = self.head
        idx = 0

        while search:
            if search.value == value:
                return f"found {search.value} at idx: {idx}"
            idx += 1
                
            search = search.next

        return None
        

def hm():
    for _ in range(3):
        print(".", end='', flush=True)
        time.sleep(.5)

    exit(1)

deque = DoublyLinkedList()

while 1:
    print("O que deseja fazer ?")
    print("[1] - Add to head")
    print("[2] - Add to tail")
    print("[3] - Remove from head")
    print("[4] - Remove from tail")
    print("[5] - Search whole list")
    print("[6] - Search items by value")
    print("Option: ")

    choice = int(input())

    match choice:
        case 1:
            value = int(input("Value to be added to head: "))
            deque.addHead(value)
        case 2:
            value = int(input("Value to be added to tail: "))
            deque.addTail(value)
        case 3:
            deque.removeHead()
        case 4:
            deque.removeTail()
        case 5:
            deque.searchList()
            input("press enter to go to the menu")
        case 6:
            value = int(input("Value to be searched in the list: "))
            search = deque.searchItemList(value)
            print(search)
            input("press enter to go to the menu")
        case _:
            hm()
