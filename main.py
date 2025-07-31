import sys
from stats import get_book_length
from stats import get_character_count
from stats import get_book_report
def main():
        if len(sys.argv) != 2:
                print("Usage: python3 main.py <path_to_book>")
                sys.exit(1)
        else:
                length = get_book_length(f"{sys.argv[1]}")
                count = get_character_count(f"{sys.argv[1]}")
                report = get_book_report(count)
                print("============ BOOKBOT ============")
                print(f"Analyzing book found at {sys.argv[1]}...")
                print("----------- Word Count ----------")
                print(f"Found {length} total words")
                print("--------- Character Count -------")
                for character in report:
                        print(f"{character["name"]}: {character["num"]}")
                print("============= END ===============")

main()
