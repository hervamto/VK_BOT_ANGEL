from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

def tokenize_large_corpus(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            tokens = word_tokenize(line)
            yield tokens

def main():
    file_path = 'yaml.txt'  # Укажите путь к вашему файлу с текстом
    tokenizer = tokenize_large_corpus(file_path)

    # Здесь вы можете выполнить дополнительные действия с полученными токенами
    for tokens in tokenizer:
        # Например, вы можете распечатать токены
        print(tokens)

if __name__ == "__main__":
    main()
