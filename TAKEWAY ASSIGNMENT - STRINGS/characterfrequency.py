# Ask user for input
text = input("\nEnter a string: ")

# Ask user if they want case sensitivity
choice = input("Ignore case? (yes/no): ")

# Convert to lowercase if ignoring case
if choice.lower() == "yes":
    text = text.lower()

# Create empty dictionary to store frequency
frequency = {}

# Count characters
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# Ask user how to sort
sort_choice = input("Sort by (1 = character, 2 = frequency): ")

# Sort results
if sort_choice == "1":
    sorted_items = sorted(frequency.items())  # sort by character
else:
    sorted_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

# Display results in table format
print("\n--- Character Frequency Table ---")
print("Character | Frequency")
print("----------------------")

for char, count in sorted_items:
    print(f"    {char}     |    {count}")