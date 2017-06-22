l = input("Input a letter of the alphabet: ")
if l in ('a','A', 'e','E', 'i','I', 'o','O', 'u','U'):
	print("%s is a vowel." % l)
elif l == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % l) 
