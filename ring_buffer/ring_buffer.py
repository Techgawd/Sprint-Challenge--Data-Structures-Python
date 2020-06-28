class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.age = 0
        self.list = []

    def append(self, item):
        size = len(self.list)
        capacity = self.capacity

        if size < capacity:
            return self.list.append(item)
        if size >= capacity:
            if self.age == self.capacity:
                self.age = 0
                self.list.insert(self.age, item)
                self.list.pop(self.age+1)
                self.age += 1
            else:
                self.list.insert(self.age, item)
                self.list.pop(self.age+1)
                self.age += 1

    def get(self):
        return self.list