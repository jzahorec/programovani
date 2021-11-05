#Datove struktury prednaska

class vagon:
    def __init__(self, hod, next=None):
        self.hod = hod
        self.next = next

class spojak:
    def __init__(self):
        self.zac = self.kon = None

    def insertz(self, co):
        self.zac = vagon(co, self.zac)
        if self.kon == None:
            self.kon = self.zac

    def insertk(self, co):
        if self.kon==None:
            self.insertz(co)
        else:
            self.kon.next = vagon(co)
            self.kon = self.kon.next

    def delete(self):
        if self.zac == None:
            return None
        else:
            nh = self.zac.hod
            self.zac = self.zac.next
            if self.zac == None:
                self.kon = None
            return nh


class fronta():
    def __init__(self):
        self.spojovyseznam = spojak()

    def enqueue(self, co):
        self.spojovyseznam.insertk(co)

    def dequeue(co):
        return self.spojovyseznam.delete()

class zasobnik():
    def __init__(self):
        self.spojovyseznam = spojak()

    def enqueue(self, co):
        self.spojovyseznam.insertz(co)

    def dequeue(co):
        return self.spojovyseznam.delete()

s = spojak()

s.insertz(1)
s.insertz(2)
s.insertk(3)
s.insertz(4)
s.insertk(5)

print(s.delete())
print(s.delete())
print(s.delete())
print(s.delete())
print(s.delete())
