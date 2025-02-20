names = {"Andi", "Abby", "Andi", "benny"}

# names[0] = "Adit"

# syntax "add" digunakan untuk menambahkan data
names.add("Tony")
print(names)

# syntax "discard" digunakan untuk menghapus data
names.discard("Abby")
print(names)

# names.remove("Abby")
# print(names)

# syntax "pop" digunakan untuk menghapus data secara acak
names.pop( )
print(names)

name = {"Andi", "Abby", "Andi", "Benny"}
friends = {"Tony", "Rendy"}

friends_list = ["Angel", "Cindy"]

# "update" digunakan untuk mengubah data yang sudah ada
name.update(friends)
print(name)

name.update(friends_list)
print(name)