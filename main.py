from stats import count_characters, count_words, items_sort, sort_on, items_unsorted, get_book_text
import sys

def main():

    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    else:
        book = sys.argv[1]
        get_book_text(book)
        text = get_book_text(book)
        num_words = count_words(text)
        counts = count_characters(text)
        chars = items_unsorted(counts)
        items_sort(chars)

        print(
        f"""    ============ BOOKBOT ============
        Analyzing book found at books/frankenstein.txt...
        ----------- Word Count ----------
        Found {num_words} total words
        --------- Character Count -------""")
        
        for item in chars:
            print(f'''    {item["char"]}: {item["num"]}''')

        print(
        """    ============= END ===============
        """
    )

main()