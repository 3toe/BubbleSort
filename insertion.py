def InsertionSort(list):
   for x in range(1, len(list), 1):
      for y in range(x, 0, -1):
         if list[y]<list[y-1]:
            list[y], list[y-1] = list[y-1], list[y]
         print(list, x, y)
   return(list)

print(InsertionSort([5,0,1,35,33,1,7]))