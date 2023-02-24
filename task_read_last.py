
def read_last(lines, txt):
    with open(txt, 'r', encoding='utf-8') as file:
        text = file.read().splitlines()
        count = int(len(text)) - int(lines)
        while count < len(text):
            print(text[count])
            count +=1

def longest_words(txt):
    with open(txt, 'r', encoding='utf=8') as file:
        text = file.read().splitlines()
        return max(text, key=len)

name_file = input('Файл: ')
lines = input('Сколько последних строк вывести: ')
read_last(lines, name_file)
print(longest_words(name_file))