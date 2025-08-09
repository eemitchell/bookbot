def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_book_word_count(book_contents):
    word_list = book_contents.split()
    return len(word_list)

def get_char_count(file_contents):
    char_set = set()
    char_count = {}
    
    for char in file_contents:
        char_set.add(char.lower())
    
    for char in char_set:
        count = 0
        for item in file_contents:
            if item.lower() == char:
                count += 1
                char_count[item.lower()] = count

    return char_count

def sort_on(items):
    return items["num"]

def sort_chars(char_dict):
    char_list = []
    for c in char_dict:
        char_list.append({"char":c, "num":char_dict[c]})
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list