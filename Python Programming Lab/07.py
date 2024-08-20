#Check Entered String is Palindrome or not
print("Palindrome" if (s := input("Enter a string: "))[::-1] == s else "Not Palindrome")