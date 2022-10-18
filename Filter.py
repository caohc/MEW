from DataBase import DataBase


def Filter(list1, label1="N/A", label2="N/A", label3="N/A", label4="N/A", label5="N/A"):
  i=5
  goal=0

  if(label5 != "N/A") :
     goal=5
  elif(label4 != "N/A") :
     goal=4
  elif(label3 != "N/A") :
     goal=3
  elif(label2 != "N/A") :
     goal=2
  elif(label1 != "N/A") :
     goal=1
 
  #print(goal)

  i=0
  n=len(list1)
  m=len(list1[0].labels)

  while i<n:
    j=0
    flag=0
    while j<m:
       if label1==list1[i].labels[j]:
          flag+=1
       elif label2==list1[i].labels[j]:
          flag+=1
       elif label3==list1[i].labels[j]:
          flag+=1
       elif label4==list1[i].labels[j]:
          flag+=1

       j+=1  

    if flag==goal:
       print(i, list1[i].English, list1[i].Chinese)
    i+=1

