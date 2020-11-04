def linearsearch (list,target):
    n = len(list)
    for i in range(n):
        if list[i] == target:
            print("targrt founded ","list: ",list,"Target: ",target)
    print("Target is not in the list.") 


def binarysearch(list,target):
    low = 0
    high= len(list)-1
    
    while low <= high:
        mid=(low + high)//2
        if list[mid]==target:
            return print("targrt founded list: ",list,"Target: ",target)
        elif target < list[mid]:
            high=mid -1
        else:
            low=mid+1
    print("Target is not in the list.") 
    
def bubblesort(list):
    n=len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    print(list)             
                
def selectionsort(list):
    for i in range(len(list)): 
        min_idx = i 
        for j in range(i+1, len(list)): 
            if list[min_idx] > list[j]: 
                min_idx = j 
              
          
        list[i], list[min_idx] = list[min_idx], list[i] 
    return list


def insertionsort(list):
    n = len(list)
    for i in range(1, n): 
        key = list[i] 
        j = i
        while j > 0 and key < list[j-1] : 
            list[j] = list[j-1] 
            j -= 1
        list[j] = key
    return list
  
def mergesort(list):
    if len(list) >1:
        mid = len(list)//2
        left_side=list[:mid]
        right_side=list[mid:]
        mergesort(left_side)
        mergesort(right_side)
        i=0
        j=0
        k=0
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                list[k]=left_side[i]
                i += 1
                k += 1
            else:
                list[k]=right_side[j]
                j += 1
                k += 1
                
        while i < len(left_side):
            list[k]=left_side[i]
            i += 1
            k += 1
            
        while j < len(right_side):
            list[k]=right_side[j]
            j += 1
            k += 1     
        
    return list        

def quicksort(list):
    quickSortHlp(list,0,len(list)-1)

def quickSortHlp(list,first,last):
    if first < last:

        splitpoint = partition(list,first,last)

        quickSortHlp(list,first,splitpoint-1)
        quickSortHlp(list,splitpoint+1,last)


def partition(list,first,last):
    pivotvalue = list[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and list[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while list[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = list[leftmark]
            list[leftmark] = list[rightmark]
            list[rightmark] = temp

    temp = list[first]
    list[first] = list[rightmark]
    list[rightmark] = temp


    return rightmark



lists=[4,5,8,2,1]
print(quicksort(lists))
print(lists)        
    
