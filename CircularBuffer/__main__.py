class circularBuffer(object):
    def __init__(self, capacity=1024):
        self.capacity = capacity
        self.buffer =[None] * self.capacity
        self.head = 0
                
    def obsBuffer(self):
        print(f"A circular buffer {self.buffer} of size {self.capacity} and head at {self.head}")
    
    def push(self, node=None):
        if not node:
            return -1
        
        self.buffer[self.head] = node
            
        self.head = (self.head + 1) % self.capacity
        
    def pop(self):
        tail = self.head
        while not self.buffer[tail]:
            tail = (tail + 1) % self.capacity

            if tail == self.head:
                return None

        self.buffer[tail] = None
            

if __name__ == "__main__":
    cBuff = circularBuffer(capacity=12)
    cBuff.obsBuffer()
    for i in range(200):
        cBuff.push(i)
        
        if (i % 17):
            cBuff.pop()
            
        cBuff.obsBuffer()