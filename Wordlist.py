import itertools

def generate_wordlist(characters, min_length, max_length, file_name="wordlist.txt"):
    with open(file_name, "w") as file:
        for length in range(min_length, max_length + 1):
            for word in itertools.product(characters, repeat=length):
                file.write("".join(word) + "\n")

# Usage:
characters = "abc123"  
min_length = 3         
max_length = 5         

generate_wordlist(characters, min_length, max_length)
print("Wordlist generated successfully!")
