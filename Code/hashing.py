def my_hash(s):
    h = 0
    for c in s:
        # add ASCII value of each character to the hash
        h += ord(c)
        # multiply by a prime number
        h *= 31
        # take modulo to keep the hash within a range
        h %= 2**32
    # convert hash value to hex and pad with leading zeros
    hash_hex = '{:08x}'.format(h)
    return hash_hex


# Prompt user to enter a string
input_str = input("Enter a string: ")

# Calculate hash value using my_hash() function
hash_val = my_hash(input_str)

# Print hash value
print("Hash value of string '", input_str, "' is", hash_val)
"""
This version of the my_hash() function converts the hash value to a hexadecimal string using Python's format() function, and pads the string with leading zeros to ensure a fixed length of 8 characters (32 bits). Note that you can adjust the length of the hash value by changing the number of characters in the format() function.
"""
