import re
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

f = open ("seneca_falls.txt")
all_text = (f.read())
all_text = str(all_text)
all_text = all_text.lower()
all_text = re.sub('[^A-Za-z]', ' ', all_text) 
print(all_text)
all_text = all_text.split()
word_text = []
for words in all_text:
    if words not in STOP_WORDS:
        word_text.append(words)
print(word_text)
#testing

def print_word_freq(file):
    pass
wordfreg = []
for w in word_text:
    all_text.append(word_text.count(w))
print("string\n" , all_text , "\n")
print("list\n" + str(word_text) + "\n")
print("frequencies\n" + str(f) + "\n")
print("pairs\n" + str(zip(word_text, f)))  






if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
