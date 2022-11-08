# Create an Artificial Intelligence that writes an essay for you

import random
import sys
import os


def main():
    # Get the text file
    if len(sys.argv) != 2:
        print("Usage: python3 essay.py filename")
        sys.exit()
    filename = sys.argv[1]
    try:
        with open(Txt.txt, "r") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        sys.exit(1)

    # Split the text into sentences
    sentences = text.split(".")

    # Create a dictionary of words and their next words
    words = {}
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence == "":
            continue
        words_list = sentence.split(" ")
        for i in range(len(words_list)):
            if i == len(words_list) - 1:
                words_list[i] = words_list[i].strip()
            if words_list[i] not in words:
                words[words_list[i]] = []
            if i == len(words_list) - 1:
                words[words_list[i]].append(".")
            else:
                words[words_list[i]].append(words_list[i + 1])

    # Generate the essay
    essay = ""
    for i in range(5):
        sentence = ""
        word = random.choice(list(words.keys()))
        while word != ".":
            sentence += word + " "
            word = random.choice(words[word])
        essay += sentence.capitalize()
    print(essay)


if __name__ == "__main__":
    main()
