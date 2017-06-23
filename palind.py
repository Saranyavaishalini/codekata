s = raw_input("enter the string")
rev = reversed(s)
if list(s) == list(rev):
   print("It is palindrome")
else:
   print("It is not palindrome")
