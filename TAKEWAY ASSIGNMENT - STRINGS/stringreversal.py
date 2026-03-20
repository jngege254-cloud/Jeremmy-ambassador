# Ask user to enter a string
text = input("Enter a string: ")

# METHOD 1: Using slicing
# This reverses the string using [::-1]
reverse1 = text[::-1]

# METHOD 2: Using a loop
# We build the reversed string one character at a time
reverse2 = ""
for char in text:
    reverse2 = char + reverse2

# Display results
print("\n--- String Reversal Results ---")
print("Original String:", text)
print("Reversed (Method 1 - slicing):", reverse1)
print("Reversed (Method 2 - loop):", reverse2)