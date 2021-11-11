class Node():
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Class():
    def __init__(self):
        self.head = self.tail = None

    def pop(self):#vybere posledni prvek
        if self.tail == None:
            return None
        elif self.tail.prev==None:
            val = self.tail.val
            self.tail = self.head = None
        else:
            val = self.tail.val
            self.tail.prev.next = None
            self.tail = self.tail.prev
        return val
    def popfirst(self):#vybere prvni prvek
        if self.head == None:
            return None
        elif self.head.next==None:
            val = self.head.val
            self.tail = self.head = None
        else:
            val = self.head.val
            self.head.next.prev = None
            self.head = self.head.next
            return val
    def append(self, v): #prida na konec
        if self.tail == None:
            self.head = self.tail = Node(v)
        else:
            self.tail.next = Node(v, prev=self.tail)
            self.tail = self.tail.next
    def prepend(self, v): #prida na zacatek
        if self.head == None:
            self.head = self.tail = Node(val)
        else:
            self.head.prev = Node(v, next=self.head)
            self.head = self.head.prev
    def reverse(self): #prohodi poradi
        tail = self.tail
        head = self.head
        act_change = self.head
        change_next = act_change.next

        while change_next != tail:
            act_change.prev, act_change.next = act_change.next, act_change.prev
            act_change = change_next
            change_next = act_change.next

        self.head = tails
        self.head.prev, self.head.next = self.head.next, self.head.prev
        self.tail = head
