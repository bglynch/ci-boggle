#--------------------------- 1. Write a Python program to calculate the sum of a list of numbers.

def sumlist(l):
    if l == []:
        return 0
    else:
        return l[0] + sumlist(l[1:])


print(sumlist([1,4,5,3,9]))

#--------------------------- 2. Write a Python program to converting an Integer to a string in any base.


#---------------------------  3. Write a Python program of recursion list sum. Go to the editor
#---------------------------  Test Data: [1, 2, [3,4], [5,6]]
#---------------------------  Expected Result: 21