def count_letters(filename):
    # Dictionary to store the count of each letter
    letter_counts = {}

    # Open the file and read its content
    with open(filename, 'r') as file:
        text = file.read()

    # Convert text to lowercase to ignore case
    text = text.lower()

    # Iterate over each character in the text
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    return letter_counts


def main():
    filename = 'yourfile.txt'  # Replace with your file name
    counts = count_letters(filename)

    # Print the letter counts
    for letter, count in sorted(counts.items()):
        print(f'{letter}: {count}')


if __name__ == "__main__":
    main()
