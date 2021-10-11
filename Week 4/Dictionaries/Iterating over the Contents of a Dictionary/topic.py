# Iterating over the contents of a dictionary
file_counts = {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23}
for extension in file_counts:
    print(extension)
# jpg
# txt
# csv
# py
for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, ext))
# There are 10 files with the .jpg extension
# There are 14 files with the .txt extension
# There are 2 files with the .csv extension
# There are 23 files with the .py extension
print(file_counts.keys())
# dict_keys(['jpg', 'txt', 'csv', 'py'])

print(file_counts.values())
# dict_keys([10, 14, 2, 23])

for value in file_counts.values():
    print(value)


# 10
# 14
# 2
# 23

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


print(count_letters("aaaaa"))
# {'a': 5}
print(count_letters("tenant"))
# {'t': 2, 'e': 1, 'n': 2, 'a': 1}
print(count_letters("a long string with a lot of letters"))
# {'a': 2, ' ': 7, 'l': 3, 'o': 3, 'n': 2, 'g': 2, 's': 2, 't': 5, 'r': 2, 'i': 2, 'w': 1, 'h': 1, 'f': 1, 'e': 2}

# Now, it's your turn! Have a go iterating over a dictionary!

# Complete the code to iterate through the keys and values of the cool_beasts dictionary.
# Remember that the items method returns a tuple of key, value for each element in the dictionary.

cool_beasts = {"octopuses": "tentacles", "dolphins": "fins", "rhinos": "horns"}
for key, values in cool_beasts.items():
    print("{} have {}".format(key, values))
# octopuses have tentacles
# dolphins have fins
# rhinos have horns
