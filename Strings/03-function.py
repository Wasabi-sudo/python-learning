course = " python for beginnERS "

print('1)', course.upper())
print('2)', course)
print('2)', course.lower()) 
print('3)', course.title()) # First letter of each word is capitalized
print('4)', course.capitalize()) # First letter of the sentence is capitalized

print('5)', course.find('y')) # Find the index of the first occurence of the character
print('6)', course.find('Y')) # Find the index of the first occurence of the character
print('7)', course.find('beginnERS')) # Find the index of the first occurence of the character

print('8)', course.replace('beginnERS', 'absolute beginners')) # Replace the first argument by the second argument

print('9)', 'python' in course) # Check if a substring is in the string
print('10)', 'python' not in course) # Check if a substring is not in the string

print('11)', course.strip()) # Remove the leading and trailing white spaces
print('12)', course.lstrip()) # Remove the leading white spaces
print('13)', course.rstrip()) # Remove the trailing white spaces

print('14)', course.split()) # Split the string into a list of words
