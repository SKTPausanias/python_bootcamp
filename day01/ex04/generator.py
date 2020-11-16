import random

def generator(text, sep=" ", option=None):
	try:
		words = text.split(sep)
		if option == "shuffle":
			for i in range(len(words) -1, 0, -1):
				j = random.randint(0, i + 1)
				words[i], words[j] = words[j], words[i]
		elif option == "unique":
			words = set(words)
		elif option == "ordered":
			words.sort()
		elif option != None:
			raise ValueError
		for each in words:
			yield each
	except TypeError:
		print("ERROR: first parameter must be a string")
	except ValueError:
		print("ERROR: Invalid option")

text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="shuffle"):
		print(word)

print()

text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="unique"):
		print(word)

print()

text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="ordered"):
		print(word)