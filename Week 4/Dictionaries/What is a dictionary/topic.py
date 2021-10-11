# The Data inside dictionaries take the form of pairs of keys and valuesl

x = {}
type(x)
# <class 'dict'>

file_counts = {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23}
print(file_counts)
# {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23}

print(file_counts["txt"])

print("jpg" in file_counts)
# True
print("html" in file_counts)
# False

file_counts["cfg"] = 8
print(file_counts)
# {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23, 'cfg': 8}
file_counts["csv"] = 17
print(file_counts)
# {'jpg': 10, 'txt': 14, 'csv': 17, 'py': 23, 'cfg': 8}

del file_counts["cfg"]
print(file_counts)

# The "toc" dictionary represents the table of contents for a book. Fill in the blanks
# to do the following:
# 1.) Add an entry for Epilogue on page 39.
# 2.) Change the page number for Chapter 3 to 24
# 3.) Display the new dictionary contents
# 4.) Display True if there is Chapter 5, False if there isn't
toc = {'Introduction': 1, "Chapter 1": 4, "Chapter 2": 11, "Chapter 3": 25, "Chapter 4": 30}
toc['Epilogue'] = 39
toc['Chapter 3'] = 24
print(toc)
print('Chapter 5' in toc)