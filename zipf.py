from tkinter import filedialog
from tkinter import *
from collections import Counter
import string
import matplotlib.pyplot as plt


def word_count(string_to_count):
    text = string_to_count

    for char in string.punctuation:
        text = text.replace(char, ' ')
    text = text.lower()

    word_list = text.split()

    return Counter(word_list).most_common()


root = Tk()

filename = filedialog.askopenfilename(
    initialdir="/",
    title="Select .txt file",
    filetypes=(("text files", "*.txt"), ("all files", "*.*"))
)

f = open(filename, "r")
count = word_count(f.read())

counts = []
for x in count:
    counts.append(x[1])

print(counts)
plt.plot(counts)
plt.ylabel("Absolute frequency of word")
plt.xlabel("Frequency rank of word")
plt.show()

root.mainloop()
