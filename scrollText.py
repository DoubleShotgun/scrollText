class scrollText:
    def __init__(self,fullText,skip,capacity):
        self.fullText = fullText
        self.skip     = skip
        self.capacity = capacity
        self.text     = fullText[:capacity]
        self.offset   = 0

    def step(self):
        if len(self.fullText) <= self.capacity:
            self.text = self.fullText
            return
            
        self.offset += self.skip
        self.offset %= len(self.fullText) + 1
        self.text = self.fullText[self.offset:self.capacity + self.offset]

        if self.offset+self.capacity >= len(self.fullText)+1:
            self.text += " "+self.fullText[:self.capacity-len(self.text)-1]

    def setString(self,fullText):
        self.fullText = fullText
        self.offset = 0
        self.text = fullText[:self.capacity]

    def __str__(self):
        self.step()
        return self.text
