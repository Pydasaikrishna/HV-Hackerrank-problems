#The included code stud will read an integer, ,form STDIN,Without using any string methods, try to print the following:
#Note that "" represents the consecutive values in between

#Sample Input 0
#3
# Sample Output 0
# 123


# n= int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(i,end=" ")

n=int(input("Emter a Number: "))
if(n<=0):
    print("Enter a positive Value!!!!")
else:
    for i in range(1,n+1):
        print(i,end=" ")