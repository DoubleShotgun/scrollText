class scrollText:
  def __init__(self,fullText,skip,capacity):
    self.fullText = fullText
    self.skip     = skip
    self.capacity = capacity
    self.text     = fullText[:capacity]
    self.count    = 0
    
  def step(self):
    self.count += self.skip
    self.count %= len(self.fullText)+1
    self.text = self.fullText[self.count:self.capacity+self.count]
    
    if self.count+self.capacity >= len(self.fullText)+1:
      self.text += " "+self.fullText[:self.capacity-len(self.text)-1]
      
  def __str__(self):
    self.step()
    return self.text
