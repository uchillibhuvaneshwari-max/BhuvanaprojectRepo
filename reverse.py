'''write a program to find the reverse of the given number'''

#num=int(input("Enter a number:"))
def reverse(num):
    rev=0
    while(num>0):
       rev=rev*10+num%10
       num//=10
    return rev

def ispalindrome(num):
    return num==reverse(num)


print(reverse (121))
<<<<<<< HEAD
print(ispalindrome(12134))
=======
print(ispalindrome(12145))
>>>>>>> b3c40cec52d906239631598a2453ca5c06a746ce



def getpalindromes(start,end):
    res=""
    for i in range(1,end+1):
        if ispalindrome(i):
            res=res+str(i)+","
    return res

print(getpalindromes(1,1000))
