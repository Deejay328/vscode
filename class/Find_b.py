# Create a string with 99 a's and one b.
# There will always be one b, but it will be at a random position from 0 to 99.
import random
letters = ['a'] * 100
b_location = random.randint(0, 99)
letters[b_location] = 'b'
letters = "".join(letters)

# Search for the letter b in the string.
# How many times will this print "Not yet" ?
print("Looking for 'b' ...")
pos = 0
while letters[pos] != 'b':
    pos += 1
    print("Not yet.")
print(f"Found it! The letter 'b' is at position {pos}." )