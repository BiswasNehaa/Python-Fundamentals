# Strings are immutable.

a="!! tom and jerry !!!"
print(len(a))
print(a.upper())
print(a.lower())

# rstrip: removes tailing characters
# only piche ka characters
print(a.rstrip("!"))

# replace() : replaces the words
print(a.replace("tom","cat"))

# Split() : convert the string into  list
print(a.split(" "))

# captalize() : change the first charac to capital and others to small
b="hello inTro "
print(b.capitalize())

str1= " Welcome to the console!!"
print(str1)
print(str1.center(50))

print(len(str1))
print(len(str1.center(50)))

print(a.count("t"))

print(a.endswith("!!!"))

print(a.find("rr"))
print(a.index("rr"))

print(a.isalnum())
print(a.isalpha())
print(a.islower())