def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = get_word_count(file_contents)
    # print(word_count)
    dic_word_count = get_dic_char_count(file_contents)
    # print(dic_word_count)
    write_report(word_count, dic_word_count)

def write_report(word_count, dic_word_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    sorted_list = get_sorted_list(dic_word_count)
    for item in sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def get_sorted_list(dic_word_count):
    sorted_list = []
    for c in dic_word_count.keys():
        if c.isalpha():
            sorted_list.append({'char':c, 'num':dic_word_count[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def get_word_count(file_contents):
    return len(file_contents.split())

def get_dic_char_count(file_contents):
    dic_char_count  = {}
    for c in file_contents.lower():
        dic_char_count[c] = dic_char_count .get(c, 0) + 1
    return dic_char_count

main()