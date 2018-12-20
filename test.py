#!/usr/local/bin/python3
list1 = [1,2,[3,4,[6,7]]]
print(list1)
def print_item(the_list):
    if (isinstance(the_list,list)):
        for m in the_list:
            print_item(m)
    else:
        print(the_list)
    


for i in list1:
    print_item(i)
