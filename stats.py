
# Count Words in a Text
def count_words(text):
    words = text.split()
    return len(words)

# Count Characters in a Text
def count_characters(text):
    low_text = text.lower()
    char_count = {}
    for ch in low_text:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1
    return char_count
   
# Print report
def print_report(freq):
    # Create an empty dictionary
    sorted_freq = {}

# While there are items left
    while freq:
        # Find the key with the maximum value
        max_key = max(freq, key=freq.get)
        if max_key.isalpha():
            print(f"{max_key}: {freq[max_key]}")
        
        del freq[max_key]
        

    
        