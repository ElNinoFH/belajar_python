import re

text = "The quick brown fox"
text += "jumps over 12 lazy dogs"

x = re.findall(r"\d", text)

print(x)

y = re.findall(r"cats", text)

print(y)