def palindrome(text):
	"""To jest funkcja, która sprawdzi
	czy tekst jest palindromem"""
	return text == text[::-1]

text = "kajak"
ispalindrome = palindrome(text)

if ispalindrome:
	print(bool(ispalindrome))
else:
	print(bool(ispalindrome))