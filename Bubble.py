def bubbleSort(list):
   for i in range(len(list)-1):
      for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
               list[j], list[j+1] = list [j+1], list[j]
   return(list)

print(bubbleSort([10000,5,2,9,5,0,2323,6,2]))

# Realizing that... 
# 1. the largest value in the list always makes its way to the 
# end on the first iteration. 
# 2. Following that, the second-largest value finds its way to 
# the penultimate position on the second iteration, and so on...
# is what I needed to understand how to do this.