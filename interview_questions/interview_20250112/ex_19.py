'''
    Q16. Read a large text file line by line without loading the whole file into memory
        file_line_by_line(filename="large_file.txt")
    Q17. Write data to a JSON file
        json_to_file(filename="data.json", data_dict={"name": "Alice", "age": 25})
    Q18. Append content to an existing file
        append_content_to_file(filename="file.txt", content="some text\n")
    Q19. Count the frequency of words in a text file
        count_words(filename = "file.txt")
'''
import json
from collections import Counter

def count_words(filename):
    with open(filename, "r") as file:
        words = file.read().split()

    word_count = Counter(words)
    print(word_count)

def append_content_to_file(filename, content):
    with open(filename, "a") as file:
        file.write(content)

def json_to_file(filename, data_dict):
    with open(filename, "w") as file:
        json.dump(data_dict, file)

def file_line_by_line(filename):
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())
