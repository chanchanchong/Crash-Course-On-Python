# Fill in the blanks to make the is_power_of function return whether the
# number is a power of the given base. Note: base is assumed to be a
# positive number. Tip: for functions that return a boolean value, you can
# return the result of a comparison.

def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        return True

    # Recursive case: keep dividing number by base.
    return is_power_of(number / base, base)


print(is_power_of(8, 2))
print(is_power_of(64, 4))
print(is_power_of(70, 10))

# 4. The count_users function recursively counts the amount of users that
# belong to a group in the company system, by going through each of the
# members of a group and if one of them is a group, recursively calling the
# function and counting the members. But it has a bug! Can you spot the
# problem and fix it?

def count_users(group):
    count = 0
    for member in get_members(group):
        count += 1
        if is_group(member):
            count += count_users(member)
    return count