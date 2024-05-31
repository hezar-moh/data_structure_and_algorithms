def sum_even_numbers(my_list):
    Sum=0
    for n in my_list:
       if n%2==0:
        Sum=Sum+n
    return Sum

my_list=[]
x=int(input("enter number of elements : "))
for i in range (1, x +1):
    y=int(input("enter intergers in a list: "))
    # my_list.append(y)

print(sum_even_numbers(my_list))