import re

text = "The quick brown fox "
text += "jumps over 12 lazy dogs!"

y = re.split(r"\s", text)

print(y)

x = re.split(r"\s", text, 20)

print(x)