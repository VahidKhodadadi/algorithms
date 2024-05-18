class Queue:  
  def __init__(self):  
      self.queue = list()  

  def add(self,data):  
      if data not in self.queue:  
          self.queue.insert(0,data)  
          return True  
      return False   

  def leng(self):  
      return len(self.queue)
  
  def peek(self):
      return self.queue[len(self.queue) - 1] 
  
  def remove(self):  
      if len(self.queue)>0:  
          return self.queue.pop()  
      return ("Empty Queue")    