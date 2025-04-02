''' exapmes for loops'''

flag=-1
for i in range(5):
    for j in range(5):
        if flag==-1:
          print(0,end=" ")
          flag*=-1
        else:
          print(1,end=" ")
          flag*=-1
    print()    
