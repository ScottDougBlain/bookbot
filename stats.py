def count_words(text):
   return len(text.split())

def count_characters(text):
    counts = {}
    cleaned_text = text.lower()
    for char in cleaned_text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def items_unsorted(counts):
    chars = []
    for key, value in counts.items():
        chars.append({
        "char": key,
        "num": value
        })
    return chars
    
def sort_on(items):
    return items["num"]

def items_sort(chars):
    chars.sort(reverse = True, key=sort_on)

def get_book_text(book):
    with open(book) as f:
        text = f.read()
    return text