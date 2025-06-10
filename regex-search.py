import re

text = "The quick brown fox "
text += "jumps over 12 lazy dogs"

x = re.search(r"\d", text)

print(x)
print(x.span())
print(x.group())