print("Le Hoa Hiep")
print("235752021610073")
def find_longest_words (text):
    words = text.split()
    max_length = max(len (word) for word in words)
    longest_words = [word for word in words if len (word) == max_length]
    return longest_words

text = "kỹ thuật lập trình"
longest_words = find_longest_words(text)
print("Những từ dài nhất:", longest_words)
