class DataBase:
   def __init__(self, array):
      self.English = array[0]
      array.remove(array[0]) 
      self.Chinese = array[0]
      array.remove(array[0])
      self.labels = array 
