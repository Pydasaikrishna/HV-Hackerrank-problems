# n=int(input("Enter the year: "))
# if (n%4==0):
#     print("The year is leap Year")
# else:
#     print("Enter the Leap Year!!!!")



#given a year,determine whether it is a leap year.if it is a leap year, return the Boolean True, otherwise retuen False:
#Note that the code stud provided reads from STDIN and passes arguments to the is_leap function
# It is only necessary to complete the is_leap function

# Sample Input : 1990
# Sample Output : False

def is_leap(year):
    leap=False

    if (year %400 == 0):
        return True
    if(year %100 == 0):
        return True
    if(year %4 == 0):
        return True
    else:
        return False
    return leap


year=int(input("Enter a Year: "))
print(is_leap(year))
