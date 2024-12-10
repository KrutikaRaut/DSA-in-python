arr=[1,2,3,5,8]
print (arr)

#taking input in array

val= int(input("enter value : "))
print(val)

#pushing an element into an array

   #1st way

arr.append(val)
print(arr)

   #2nd way

arr.insert(2,val)
print(arr)

# to delete an element

    #1st way

arr.pop()
print(arr)

    #2nd way

arr.remove(2)
print(arr)

#slicing in an array

print(arr[1:5])
print(arr[-4:-2])

#min and max element in an arr

print(min(arr))
print(max(arr))

#sum of all element in an array

print("sum of all elements in an array : ", sum(arr))

#sorting an array

arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

#to make a copy of array

arr1=arr.copy()




