#sample_list = [23,3,4,"somu"]
#print(type(sample_list))

#smaple_list = [2,3,4,"sowmu"]
#print(id(sample_list))
#sample_list.append("somu ")
#print(sample_list)
#print(id(sample_list))

#example_list = [1,2,3,"somu"]
#print(id(example_list))
#example_list.append("somu")
#print(example_list)


#my_list = []
#print(my_list)
#print(type(my_list))

#my_list = [1,2,3,"sowmya","vara",(1,2,3),[5,6,7],{7,8,9}]
#print(my_list)
#print(type(my_list))


#my_list = [10,20,30,40,50]
#sub = my_list [1:3]
#print(sub ,my_list)


#my_list = [10,20,30,40,50,60]
#sub = my_list [0:8]
#sub = my_list [1:3]
#sub = my_list [0:2]
#sub = my_list [0:5]
#print(sub ,my_list)


#my_list = [10,20,30,40,50,60,70,80]
#print(my_list[0:8:2])
#print(my_list[0:8:3])
#print(my_list[0:8:4])
#print(my_list[::])

# FORVARD DIRECTION:

#my_list = [10,20,30,40,50]
#print(my_list[-0:-1])

#list= [10,20,30,40,50]
#print(list[-3:])

# BASED VALUE:
# POSITIVE:
#list = [10,20,30,40,50,60]
#print(list[0:4:-1])
#print(list[3::-1])


# NEGATIVE:
#list =[10,20,30,40,50,60]
#print(list[-7:-2:])
#print(list[:-6:-1])

#list =[[1,4,2],[5,6,7],[9,2,7]]
#print(list[1][2])
#print(list[1][0])
#print(list[2][2])

#numbers = [3,4,5,6,7,8]
#numbers.append("pythonlife")
#print(numbers)
#numbers.extend([1,2,3,4])
#numbers.extend(["python"])
#print(numbers)
#sample =  numbers.copy()
#sample.append("sowmya")
#print(sample)
#print(f"original list {numbers}")

#numbers = [3,4,5,6,7,8]
#numbers.clear()
#print(numbers)

#numbers = [1,1,22,3,4,56,8,8,8,9]
#print(numbers.count(1))
#print(numbers.count(22))
#print(numbers.count(8))

#numbers = [1,1,22,3,4,56,8,8,8,9]
#print(numbers.index(1))
#print(numbers.index(22))
#print(numbers.index(56))


#numbers = [1,1,22,3,4,56,8,8,8,9]
#numbers.removes(4)
#print(numbers)

#numbers = [1,2,3,4,5]
#obj=numbers.pop(2)
#print(numbers)
#print(obj*10)

#numbers = [1,1,22,3,4,56,8,8,8,9]
#numbers.insert(0,"python")
#print(numbers)

#numbers = [1,1,22,3,4,56,8,8,8,9]
#numbers.reverse()
#print(numbers)

# assorting and disorting:
#numbers = [1,1,22,3,4,56,8,8,8,9]
#numbers.sort(reverse=True)
#print(numbers)

#list = []
#for i in range(11):
    #if i%2==0:
       # list.append(i)
#print(list)

#list = []
#for i in range(22):
    #if i%2==0:
      #  list.append(i)
#print(list)

# syntax:
#result = [i for i in range(11) if i%2==0]
#print(result)

#list = []
#for i in range(11):
    #result = i**2
    #list.append(result)
#print(list)

#numbers = [1,1,22,3,4,56,8,8,8,9]
#print(len(numbers))

# remove:
#numbers = [1,1,22,3,4,56,8,8,8,9,5,5,5,5,6,6,7,8]
#for i in numbers:
    #if i == 1:
        #numbers.remove(i)
    #print(numbers)

#numbers = [1,1,22,3,4,56,8,8,8,9,5,5,5,5,6,6,7,8]
#list = []
#for i in numbers:
    #if i!=5:
     #   list.append(i)
    #print(numbers)



 #numbers = [1,1,22,3,4,56,8,8,8,9]
#print(numbers.index(1))
#print(numbers.index(22))
#print(numbers.index(56))

# index:
#numbers = [1,1,22,3,4,56,8,8,8,9]
#list = []
#for i in numbers:
   # if i==0:
  #   numbers.index(3)
#print(numbers)

# TASK ;
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
list = []
for i in list1:
    for j in list2:
        if i ==j:
            list.append(i)
print(list)

list = [1,2,2,3,4,4,5]
sample_list = []
for i in list:
    if i not in sample_list:
     print(sample_list)

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
print(list1,list2)

list = [1,2,3,4,5]
result=list*3
print(result)

numbers = [1,2,3,4,5,5]
numbers.remove(5)
print(numbers)

list = [1,2,3,4,5,6]
list.insert(1,"python")
print(list)

word = ["apple,","banana","cherry","date"]
print(len(word))


numbers = [1,2,3,4,5,6,7,8,9,10]
square = [x **2 for x in numbers]
print(square)

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in list:
    if i%2==0:
        print(list)


