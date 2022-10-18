# Программа подсчета слов в файле
import os
import sys


print(
f'Вам доступны следующие команды:\n',
f'1) load  — загрузить слова из файла filename.txt;\n',
f'2) wordcount проверочное слово — отобразить число раз, которое программа встретила слово\n'
f'3) clear-memory — очистить все данные о прочитанных словах из памяти.\n'
)
command = input("Введите комманду:")

def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def main():
    if command == 'load':
        filename = input("Введите путь к файлу: ")
        if not os.path.exists(filename):
            print("Указанный файл не существует")
        else:
            words = get_words(filename)
            words_dict = get_words_dict(words)
            print(f"Кол-во слов: {len(words)}")
            print(f"Кол-во уникальных слов: {len(words_dict)}")
            print("Все использованные слова:")
            for word in words_dict:
                print(word.ljust(20), words_dict[word])
    if command == 'clear-memory':
            restart_program()


if __name__ == "__main__":
    main()
