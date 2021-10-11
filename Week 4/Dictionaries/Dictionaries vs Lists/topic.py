# Dictionaries vs Lists
ip_addresses = ["192.168.1.1", "127.0.0.1", "8.8.8.8"]
host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}

# You want to use dictionaries when you plan on searching for a specific element

# In Python, a dictionary can only hold a single value for a given key. To workaround this,
# our single value can be list containing multiple values. Here we have a dictionary called
# "wardrobe" with items of clothing and their colors. Fill in the blanks to print a line
# for each item of clothing with each color, for example: "red tshirt", "blue tshirt", and so on.

wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
for item, colors in wardrobe.items():
    for color in colors:
        print("{} {}".format(color, item))

# Set
# Used when you want to store a bunch of
# elements and be certain that they're only
# present once
