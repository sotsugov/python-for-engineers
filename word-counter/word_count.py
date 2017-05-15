#! /usr/bin/python
import sys


def count_words(data):
    return len(data.split())


def count_lines(data):
    return (len([l for l in data.split("\n") if l]))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python word_count.py <file>")
        exit(1)

    filename = sys.argv[1]
    f = open(filename, "r")
    data = f.read()
    f.close()

    num_words = count_words(data)
    num_lines = count_lines(data)

    print("The number of words: ", num_words)
    print("The number of lines: ", num_lines)
