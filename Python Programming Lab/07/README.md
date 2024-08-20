# Palindrome Checker in One Line

How to convert a multi-line Python script to a single-line expression for checking if a string is a palindrome.

## Multi-Line Code

First, let’s look at the multi-line version of the palindrome checker:

```python

# Get input from the user
s = input("Enter a string: ")

# Reverse the string
reversed_s = s[::-1]

# Check if the reversed string is equal to the original string
if reversed_s == s:
    print("Palindrome")
else:
    print("Not Palindrome")
```

### Explanation
```python
# Prompts the user to enter a string and stores it in the variable s.
s = input("Enter a string: ")

# Reverses the string s and stores it in reversed_s.
reversed_s = s[::-1]

# Compares the reversed string to the original string.
if reversed_s == s:

# Prints the result based on whether the reversed string matches the original string.
print("Palindrome") and print("Not Palindrome")
```

## One-Line Code

```python
print("Palindrome" if (s := input("Enter a string: "))[::-1] == s else "Not Palindrome")
```

### Explanation

```python

# The walrus operator := is used to both assign the input string to the variable s and use it immediately in the expression.
s := input("Enter a string: ")

# Reverses the string s.
s[::-1]

# Checks if the reversed string is equal to the original string.
s[::-1] == s

# Conditional expression that prints "Palindrome" if the condition is true, otherwise "Not Palindrome".
"Palindrome" if ... else "Not Palindrome"

