text = input()
text = list(text)
rev_text = []

for i in reversed(text):
    rev_text.append(i)

for i in range(len(rev_text)):
    print(rev_text[i], end="")
