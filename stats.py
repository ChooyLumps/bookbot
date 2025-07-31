def get_book_length(file_path):
        with open(file_path) as f:
                file_contents = f.read()
        words = file_contents.split()
        length = len(words)
        return length
def get_character_count(file_path):
        letters_dict = {}
        with open(file_path)as f:
                file_contents = f.read()
        lowered_contents = file_contents.lower()
        words = lowered_contents.split()
        for word in words:
                for char in word:
                        letters_dict[char] = 0
        for word in words:
                for char in word:
                        letters_dict[char] += 1
        return letters_dict

def sort_on(items):
        return items["num"]

def get_book_report(letters_dict):
        character_list = []
        for letter in letters_dict:
                letter_info = {}
                if letter.isalpha() == True:
                        letter_count = letters_dict[f"{letter}"]
                        letter_info = {"name": letter, "num": letter_count}
                        character_list.append(letter_info)
        character_list.sort(reverse=True, key=sort_on)
        return character_list
