# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

string = input("Please enter a string for palindrome checking: ")

string2 = string[::-1]

if string2 == string:
    print(string, "is a palindrome")
else:
    print("given string is not a palindrome, sorry!")
