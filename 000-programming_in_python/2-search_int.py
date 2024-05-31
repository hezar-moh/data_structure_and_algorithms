def find_first_occurence(my_list, num):
    if num in my_list:
       
       for i in range(len(my_list)):
           if my_list[i]== num:
               return i
    else:
        return None

        
my_list=[]
x=int(input("enter number of elements : "))
for i in range (1, x +1):
    y=int(input("enter intergers in a list: "))
    my_list.append(y)
num=int(input("enter a num : "))
print(find_first_occurence(my_list,num))