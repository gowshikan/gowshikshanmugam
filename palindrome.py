my_str = 'aIbohPhoBiA'
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) ==list(rev_str):
print("it is palindrome")
else:
print("it is not palindrome")
