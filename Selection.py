def selectionSort(list):
   for i in range(len(list)):
      for j in range(i,len(list),1):
         if list[j] < list[i]:
            list[i], list[j] = list[j], list[i]
   return(list)

# test
print(selectionSort([999,2,454,2, -3, 0, 34]))