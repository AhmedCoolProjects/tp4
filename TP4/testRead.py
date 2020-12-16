file = input('name of the file you want to read : ')
f = open(file, 'r')
text = f.read()
print(text)