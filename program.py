with open('referat.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    file_len = len(text)
    file_words = len(text.split())
    text = text.replace('.', '!')
    print(file_len)
    print(file_words)

    with open('referat2.txt', 'w', encoding='utf-8') as file:
        file.write(text)
