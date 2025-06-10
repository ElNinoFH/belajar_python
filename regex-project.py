import re

text = "Nama saya Nino, saya berumur 15 tahun"

x = re.search(r"\d", text)
print(x)
print(x.span())
print(x.group())

y = re.split(r"\s", text)
print(y)

z = re.sub(r"\s", "_", text, 2)
print(z)