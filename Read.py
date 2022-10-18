from DataBase import DataBase

def Read(list1, i):
  if i==0:
     f = open("word.txt")
  else :
     f = open("sentence.txt")
  line = f.readline()
  i=0

  #print("数据读取:")
  while line:
     data=line.replace('\n', '')
     array=data.split('\t')
     a=DataBase(array)
     list1.append(a)
     #print(list1[i].English, list1[i].Chinese, list1[i].labels)
     line = f.readline()
     i+=1
  f.close()


